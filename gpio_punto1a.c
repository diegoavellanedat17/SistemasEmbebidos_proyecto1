#include <stdio.h>
#include <wiringPi.h>
// Incluir las librerias correspondientes al standard input output y a wiringPi para asignacion de GPIO
int main(){
    //Inicializar el Wiring Pi 5
    const int led = 5;
    // Definir el PIN como OUTPUT
    wiringPiSetup();
    pinMode(led, OUTPUT);
    // Ciclo de cambio del PIN
    while (1) {
        digitalWrite(led, HIGH);
        digitalWrite(led, LOW);
    }
   return 0;
}
