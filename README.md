# Proyecto 1 de Sistemas Embebidos - GPIO y one-wire en Raspberry Pi

Proyecto 1 de la materia Sistemas Embebidos de la Pontificia Universidad Javeriana

<p align="center">
<img src="https://github.com/diegoavellanedat17/SistemasEmbebidos_proyecto1/blob/main/RPI.jpeg" alt="drawing" width="1000"/>  
</p>

En un sistema embebido desarrollado con el objetivo de cumplir con necesidades especificas, existen características como tiempos de ejecución y capacidad de procesamiento priorizadas como base para el diseño electrónico.

En el presente proyecto se expone el diseño, la ejecución y el protocolo de pruebas del manejo de GPIO (General Purpose Input/Output, Entrada/Salida de propósito general) en diferentes lenguajes como C, Bash y Python. Esto con el objetivo de comparar aspectos como complejidad, tiempos de ejecución, costo de procesamiento y desarrollo en un sistema embebido particular. También se exponen las diferentes alternativas para adquirir información de un sensor DS18B20 y guardarlos en archivos de texto.

### Contenidos

A continuación se hará un breve resumen de los contenidos del repositorio.

| Archivo | Ubicación |
| ------ | ------ |
| GPIO C | [/gpio_punto1a.c](https://github.com/diegoavellanedat17/SistemasEmbebidos_proyecto1/blob/main/gpio_punto1a.c) |
| GPIO Python | [/gpio_punto1b.py](https://github.com/diegoavellanedat17/SistemasEmbebidos_proyecto1/blob/main/gpio_punto1b.py)|
| GPIO Bash | [/led.sh](https://github.com/diegoavellanedat17/SistemasEmbebidos_proyecto1/blob/main/led.sh)|
| OneWire Python | [/temperatura_punto2.py](https://github.com/diegoavellanedat17/SistemasEmbebidos_proyecto1/blob/main/temperatura_punto2.py) |
| OneWire Bash | [/temp.sh](https://github.com/diegoavellanedat17/SistemasEmbebidos_proyecto1/blob/main/temp.sh) |


### Ejecución

Para ejecutar el código de C en consola se realiza lo siguiente:

```
gcc -o gpio_punto1a gpio_punto1a.c -l wiringPi
./gpio_punto1a
```

Para ejecutar los códigos de Python en consola se realiza lo siguiente:

```
python3 ./gpio_punto1b.py
```

```
python3 ./temperatura_punto2.py
```

Para ejecutar los códigos de bash en consola se realiza lo siguiente:

```
bash ./led.sh
```

```
bash ./temp.sh
```

<p align="center">
<img src="https://github.com/diegoavellanedat17/SistemasEmbebidos_proyecto1/blob/main/Sensor.jpeg" alt="drawing" width="1000"/>  
</p>

### Desarrollado por

- :desktop_computer: [Diego Fernando Avellaneda Torres](https://github.com/diegoavellanedat17)

- :computer: [Andrea Juliana Ruiz Gómez](https://github.com/andrearuizg)
