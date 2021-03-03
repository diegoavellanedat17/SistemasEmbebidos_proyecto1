#!/bin/bash

# Path para acceso a GPIO
GPIO_PATH=/sys/class/gpio

# Asignacion de GPIO al led 
LED=17

# Estados
ON="1"
OFF="0"

# Eliminamos la entrada del puerto GPIO  
echo $LED > $GPIO_PATH/unexport 

# Exportamos el puerto GPIO
echo $LED > $GPIO_PATH/export 

# Se configura el puerto GPIO como salida
echo out > $GPIO_PATH/gpio$LED/direction 

# Apagar led
echo $OFF > $GPIO_PATH/gpio$LED/value

while [ 1 ]
do
  # ON
#Encendemos el LED asignandole 1 como valor lógico
  echo $ON > /sys/class/gpio/gpio$LED/value
 
  # OFF
  echo $OFF > /sys/class/gpio/gpio$LED/value
done
