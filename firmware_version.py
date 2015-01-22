import time
import grovepi
from grove_oled import *

# Connect the OLED module to port I2C-1
oled_init()
oled_clearDisplay()
oled_setNormalDisplay()
oled_setVerticalMode()
time.sleep(.1)


# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# SIG,NC,VCC,GND
sensor = 4

while True:
    try:
        [temp,humidity] = grovepi.dht(sensor,1)
        print "temp =", temp, " humidity =", humidity
        oled_setTextXY(0,0)
    	oled_putString("Temp= "+ str(temp)+"C")
    	oled_setTextXY(1,0)
    	oled_putString("Hum= "+ str(humidity))
        time.sleep(30)
    except IOError:
        print "Error"
    except TypeError:
    	print "Error"