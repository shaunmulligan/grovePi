import time
import grovepi
from grove_oled import *

oled_init()
oled_clearDisplay()
oled_setNormalDisplay()
oled_setVerticalMode()
time.sleep(.1)

print "hello world to screen"
for i in range(0,12):
    oled_setTextXY(i,0)
    oled_putString("Hello World")

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# SIG,NC,VCC,GND
sensor = 4

while True:
    try:
        [temp,humidity] = grovepi.dht(sensor,1)
        print "temp =", temp, " humidity =", humidity
        time.sleep(30)
    except IOError:
        print "Error"
    except TypeError:
    	print "Error"