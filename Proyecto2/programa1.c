#include <stdio.h>
#include<stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
// Incluir las librerias correspondientes al standard input output y a wiringPi para asignacion de GPIO
int main(){
    //Inicializar el Wiring Pi 5
    const int led = 5;
    const int tm = 2;
    // Definir el PIN como OUTPUT
    wiringPiSetup();
    pinMode(led, OUTPUT);
    // Ciclo de cambio del PIN
    while (1) {
        digitalWrite(led, HIGH);
        usleep(tm);
        digitalWrite(led, LOW);
        usleep(tm);
    }
   return 0;
}
