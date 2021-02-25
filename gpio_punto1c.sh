#!/usr/bin/env bash

#Generar un ciclo y con el comando gpio write y read activar el GPIO
while true; do
	gpio write 5 1
	gpio write 5 0
done
