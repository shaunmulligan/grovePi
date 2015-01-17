#!/usr/bin/python
import smbus
import time
import math
import RPi.GPIO as GPIO
import struct

from subprocess import call

call(["i2cdetect", "-y 1"])
