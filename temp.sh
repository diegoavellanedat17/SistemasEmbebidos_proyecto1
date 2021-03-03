#!/bin/bash

FN="$(date +%Y%m%d)_TEMPERATURA.csv"
echo "Date;Temperature;" > $FN
while [ 1 ]
do
#TEMP=$(echo "scale=3;$(cat /sys/bus/w1/devices/28-3c01d0756fd5/temperature)/1000" | bc -l)
TEMP=$(echo "scale=3;$(cat /sys/bus/w1/devices/28-030797940f24/temperature)/1000" | bc -l)
echo "$(date +%Y%m%d) $(date +%H%M%S);$TEMP;" >> $FN
sleep 10
done
