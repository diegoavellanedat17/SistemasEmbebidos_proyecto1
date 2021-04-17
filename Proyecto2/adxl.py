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
ser = serial.Serial('/dev/ttyAMA0', 115200)
ser = serial.Serial('/dev/ttyUSB0', 115200)

#RP -> SERIAL - PROMEDIO
#(SERIAL <- RP) -> TRAMA###
#SERISL - RP - TRAMA ###
aceleracion = []
x = []
y = []
z = []

qG = queue.Queue()
qP = queue.Queue()
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
        ser.write(ms.encode())
        time.sleep(0.4)
        qP.task_done()

def worker3():
    #global qG # no es necesario ya en Py3!
    while True:
        #print(f'Aceleracion promedio = ',item)
        rd = ser.readline()
        print("hilo 3")
        print(rd)
        time.sleep(0.4)
#str = "##"+PR+"-"+N"-##\n"

while True:
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


    #threading.Thread(target=worker3, daemon=True).start()
    rd = ser.readline()
    print("hilo 3")
    print(rd)
    #print('Se terminan de enviar los trabajos a la cola\n', end='')
    qG.join()
    #print('Se terminan de realizar los trabajos')
