# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import adafruit_adxl34x
import threading
import queue
import numpy as np
import serial

i2c = busio.I2C(board.SCL, board.SDA)

# For ADXL345
accelerometer = adafruit_adxl34x.ADXL345(i2c)

#Inicializamos el puerto de serie a 115200 baud
ser_1 = serial.Serial('/dev/ttyAMA0', 115200)
ser_2 = serial.Serial('/dev/ttyUSB0', 115200)

#RP -> SERIAL - PROMEDIO
#(SERIAL <- RP) -> TRAMA###
#SERISL - RP - TRAMA ###
aceleracion = []

qG = queue.Queue()
qP = queue.Queue()
qS = queue.Queue()
def worker():
    #global qG # no es necesario ya en Py3!
    while True:
        item = qG.get()
        #print(f'Aceleracion = ',item)
        time.sleep(0.2)
        qG.task_done()

def worker2():
    #global qG # no es necesario ya en Py3!
    while True:
        item = qP.get()
        print("Hilo 2")
        #print(f'Aceleracion promedio = ',item)
        ms = str(item)+"\n"
        print(ms)
        ser_1.write(ms.encode("utf-8"))
        time.sleep(0.2)
        qP.task_done()

def worker3():
    #global qG # no es necesario ya en Py3!
    while True:
        #print(f'Aceleracion promedio = ',item)
        #rd = ser_2.readline()
        #rd = rd.decode("utf-8")
        item = qS.get()
        print("hilo 3")
        print(item)
        time.sleep(0.2)
        qS.task_done()
#str = "##"+PR+"-"+N"-##\n"


while True:
    x = []
    y = []
    z = []

    threading.Thread(target=worker, daemon=True).start()
    N=10

    for item in range(N):
        aceleracion = np.asarray(accelerometer.acceleration)
        x.append(aceleracion[0])
        y.append(aceleracion[1])
        z.append(aceleracion[2])
        qG.put(aceleracion)
        time.sleep(0.2)

    threading.Thread(target=worker2, daemon=True).start()
    prom = [np.sum(x)/N, np.sum(y)/N, np.sum(z)/N]
    qP.put(prom)
    #print(prom)
    #print(type(prom))


    threading.Thread(target=worker3, daemon=True).start()
    rd_2 = ser_2.readline()
    rd_2 = rd_2.decode("utf-8")
    qS.put(rd_2)

    #print("hilo 3")
    #print(rd)
    #print('Se terminan de enviar los trabajos a la cola\n', end='')
    qG.join()
    #print('Se terminan de realizar los trabajos')
