## @package Proyecto 2
# Multi hilos, One-wire, I2C, serial
# 
#  @version 1 
#
# Pontificia Universidad Javeriana
# 
# Ingeniería Electrónicq
# 
# Desarrollado por:
# - Andrea Juliana Ruiz Gomez
#       Mail: <andrea_ruiz@javeriana.edu.co>
#       GitHub: andrearuizg
# - Diego Fernando Avellaneda Torres
#       Mail: <avellanedad@javeriana.edu.co>
#       GitHub: diegoavellanedat17

# Declaración de módulos
import time
import board
import busio
import adafruit_adxl34x
import threading
import queue
import numpy as np
import serial
import sys 
import subprocess

## Temperatura
# Guarda el valor de la temperatura en un archivo .csv
def worker1():
    while True:
        item = qT.get()
        #print('Temperatura = ',item)
        file = open(filename, "a")  # append mode 
        file.write(item) 
        file.close() 
        time.sleep(1)
        qT.task_done()


## Aceleración
# Muestra el valor de la aceleración en la pantalla
def worker2():
    while True:
        item = qG.get()
        print('Aceleracion = ',item)
        time.sleep(0.2)
        qG.task_done()


## Serial - enviar
# Envía valor por serial
def worker3():
    while True:
        item = qP.get()
        #print("Se envío = ", item)
        ms = str(item)+"\n"
        ser_1.write(ms.encode("utf-8"))
        time.sleep(0.4)
        qP.task_done()


## Serial - recibir
# Recibe valor por serial
def worker4():
    while True:
        item = qS.get()
        if (item.startswith("##") and item.endswith("-##")):
            print("Se recibió = ", item)
        time.sleep(0.4)
        qS.task_done()


if __name__ == "__main__":
    # Configuración I2C 
    i2c = busio.I2C(board.SCL, board.SDA)

    # Para ADXL345
    accelerometer = adafruit_adxl34x.ADXL345(i2c)

    #Inicializamos los puertos del serial a 115200 baud
    ser_1 = serial.Serial('/dev/ttyAMA0', 115200)
    ser_2 = serial.Serial('/dev/ttyUSB0', 115200)

    # Declaración de aceleración
    aceleracion = []

    # Declaración de colas
    qT = queue.Queue()
    qG = queue.Queue()
    qP = queue.Queue()
    qS = queue.Queue()
    qM = queue.Queue()

    # Declaración del nombre del archivo donde se va a guardar la temperatura en el formato YYYMMDD_TEMPERATURA.csv
    filename=subprocess.run(["date","+%Y%m%d_TEMPERATURA.csv"],stdout=subprocess.PIPE,text=True)
    filename=filename.stdout.rstrip("\n")

    # Definir el factor por el que debe dividirse la temperatura
    TEMP_FACTOR=1000

    x = []
    y = []
    z = []

    while True:
        # Hilo 1- Guardar temperatura 
        threading.Thread(target=worker1, daemon=True).start()
        fecha_dato = subprocess.run(["date","+%Y%m%d %H%M%S"],stdout=subprocess.PIPE,text=True)
        fecha_dato=fecha_dato.stdout.rstrip("\n")
        temperatura = subprocess.run(["cat","/sys/bus/w1/devices/28-030797943f92/temperature"],stdout=subprocess.PIPE,text=True)
        temperatura= str(int(temperatura.stdout)/TEMP_FACTOR)
        trama_guardar=fecha_dato+' '+temperatura+'\n'
        qT.put(trama_guardar)

        # Hilo 2 - Mostrar aceleración
        N=10

        #for item in range(N+5):
        aceleracion = np.around(np.asarray(accelerometer.acceleration), decimals=1)
        x.append(aceleracion[0])
        y.append(aceleracion[1])
        z.append(aceleracion[2])
        
        qG.put(aceleracion)
        threading.Thread(target=worker2, daemon=True).start()

        # Hilo 3 - Enviar promedio por serial
        if(len(x) > N):
            prom = np.around([np.sum(x[len(x)-N:len(x)])/N, np.sum(y[len(y)-N:len(y)])/N, np.sum(z[len(z)-N:len(z)])/N], decimals=1)
            prom_s = "##"+str(prom)+"-"+str(N)+"-##\n"
            qP.put(prom_s)
        else: 
            prom = np.around([np.sum(x)/len(x), np.sum(y)/len(y), np.sum(z)/len(z)], decimals=1)
            prom_s = "##"+str(prom)+"-"+str(N)+"-##\n"
            qP.put(prom_s)
        threading.Thread(target=worker3, daemon=True).start()

        # Hilo 4 - Leer serial
        rd_2 = ser_2.readline()
        rd_2 = rd_2.decode("utf-8")
        rd_2 = rd_2.rstrip("\n")
        qS.put(rd_2)
        threading.Thread(target=worker4, daemon=True).start()

        qG.join()
