#!/usr/bin/env python
import time
import re

sensor = '/sys/bus/w1/devices/28-020c9245ad30/w1_slave'


def readTempSensor(sensorName):
    """Aus dem Systembus lese ich die Temperatur der DS18B20 aus."""
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    m = re.search(".*t=(\d+)", lines[1])
    return float(m.group(1))/1000


while True:
    print(time.strftime('%H:%M:%S') + " - " + str(readTempSensor(sensor)))
    time.sleep(1)
