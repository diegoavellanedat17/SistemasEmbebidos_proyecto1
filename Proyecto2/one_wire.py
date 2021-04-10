
# Importar las dependencias para usar los subprocesos de la linea de comandos, del sistema y el tiempo para guardar los datos
import sys 
import subprocess
import time

#Guardar en una variable el nombre del archivo donde se va a guardar la información en el formato YYYMMDD_TEMPERATURA.csv
#El archivo se guarda sin el \n
#Definir el factor por el que debe dividirse la temperatura
filename=subprocess.run(["date","+%Y%m%d_TEMPERATURA.csv"],stdout=subprocess.PIPE,text=True)
filename=filename.stdout.rstrip("\n")
TEMP_FACTOR=1000
#print(filename)

#Ciclo de recoleccion de datos
#Guardar en una variable la fecha del dato
#Guardar en otra variable la temperatura encontrada en el archivo del sensor DS18b20,
#La variable de temepratura debe dividirse en 1000 y agregarse a la trama
#Abrir escribir el archivo y cerrarlo en cada ciclo

while True:
	
	fecha_dato = subprocess.run(["date","+%Y%m%d %H%M%S"],stdout=subprocess.PIPE,text=True)
	fecha_dato=fecha_dato.stdout.rstrip("\n")
	temperatura = subprocess.run(["cat","/sys/bus/w1/devices/28-3c01d0754b88/temperature"],stdout=subprocess.PIPE,text=True)
	temperatura= str(int(temperatura.stdout)/TEMP_FACTOR)
	trama_guardar=fecha_dato+' '+temperatura+ '\n'
	print(trama_guardar)
	file = open(filename, "a")  # append mode 
	file.write(trama_guardar) 
	file.close() 
	time.sleep(10)

