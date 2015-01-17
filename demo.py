#!/usr/bin/python
import smbus
import time
import math
import RPi.GPIO as GPIO
import struct

from subprocess import call
print "checking i2c"
call(["i2cdetect -y 1", ], shell=True)
