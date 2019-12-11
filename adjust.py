#!/usr/bin/env python
import time

sensor = '/sys/bus/w1/devices/28-020c9245ad30/w1_slave'


def readTempSensor(sensorName):
    """Aus dem Systembus lese ich die Temperatur der DS18B20 aus."""
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    return lines


while True:
    print(time.strftime('%H:%M:%S') + " - " + str(readTempSensor(sensor)))
    time.sleep(1)
