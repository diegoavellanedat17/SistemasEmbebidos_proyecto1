#include <stdio.h>
#include <time.h>
#include <wiringPi.h>
#include <unistd.h>




void DelayMicrosecondsNoSleep (int delay_us);
int main()
{
    int x;
    const int led = 5;

    wiringPiSetup();
    pinMode(led, OUTPUT);
    // Ciclo de cambio del PIN
    while (1) {
        digitalWrite(led, HIGH);
        DelayMicrosecondsNoSleep(2.5);
        digitalWrite(led, LOW);
        DelayMicrosecondsNoSleep(2.5);
    }

    return(0);
}


void DelayMicrosecondsNoSleep (int delay_us)
{
    long int start_time;
    long int time_difference;
    struct timespec gettime_now;

    clock_gettime(CLOCK_REALTIME, &gettime_now);
    start_time = gettime_now.tv_nsec;       //tomar el valor en nanosegundos
    while (1)
    {
        clock_gettime(CLOCK_REALTIME, &gettime_now);
        time_difference = gettime_now.tv_nsec - start_time;
        if (time_difference < 0)
            time_difference += 1000000000;              // Ir sumando cada segundo
        if (time_difference > (delay_us * 1000))        //Delay por nanosegundos 
            break;
    }
}