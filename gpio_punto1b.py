import time
import RPi.GPIO as GPIO
#Incluir Libreria para manejo de pines GPIO

#Definir pin 24 en BCM o 5 en WiPi
output_pin = 24

# Deshabilitar Warnings cuando se ejecuta el código
GPIO.setwarnings(False)

# Manjear la asignacion en BCM
GPIO.setmode(GPIO.BCM)

#Definir como salida
GPIO.setup(output_pin, GPIO.OUT)

while True:
    GPIO.output(output_pin, GPIO.HIGH) # GPIO ON
    GPIO.output(output_pin, GPIO.LOW)  # GPIO OFF

