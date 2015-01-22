#GrovePi board with Resin.io

This project demonstrates the use of the [GrovePi][grovepi-link] Raspberry Pi addon board deployed using the resin.io service.

For those that don't know, the GrovePi board allows the Raspberry Pi to interface with hundreds of Grove sensors developed by [Seeedstudio][seeedstudio-link]. Resin.io is a modern devOps service for IoT deploments. It allows you to deploy whole swarms of connected devices with a simple `git push`.

In this project we will simply read the temperature and humidity reading from the [DHT-22 sensor][hum-sensor-link] and display these values on the small [OLED Grove module][oled-link].

## What you will need:

* 1 or 100 Raspberry Pi B/B+'s
* A micro SD card
* A usb wifi adaptor
* A micro usb cable for power
* GrovePi board [link][grovepi-link]
* Humidity sensor [link][hum-sensor-link]
* 0.96" OLED display [link][oled-link]

## Get Setup on Resin.io
Head over to ["Getting Started with Resin.io"][getting-started] so you can start deploying code updates to your raspberry pis. Once you successfully have your Pi online and running code, its time to setup the hardware.

## Connecting up the Hardware

Mount the GrovePi to the raspberry pi. If you are using a B+ it is neccessary to cover the bottom of the GrovePi board with insulation tape so that the bottom contacts don't short on the Pi's USB ports. It is explained in more detail over [here][grovepi-setup].

Now connect up the DHT-22 humidity sensor to port D4 and the OLED module to I2C-1 on the GrovePi. 

Now clone this repo and push it to your resini.io application endpoint and in a short while you should see a stream of temperature and humidity readings logging in the console on your resin.io dashboard. You should also see the same values reflected on the small OLED display.

As an extension to this project you could also log and store the values to a cloud store like firebase. There is an awesome python module for firebase called [python-firebase][python-firebase-link].

Happy hacking...

[grovepi-link]:http://www.dexterindustries.com/GrovePi/
[seeedstudio-link]:http://www.seeedstudio.com/depot/category_products?themes_id=1417
[hum-sensor-link]:http://www.seeedstudio.com/depot/Grove-TemperatureHumidity-Sensor-Pro-p-838.html?cPath=25_125
[oled-link]:http://www.seeedstudio.com/depot/Grove-OLED-Display-096-p-824.html
[getting-started]:http://docs.resin.io/#/pages/gettingStarted.md
[grovepi-setup]:http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/raspberry-pi-model-b-grovepi/
[python-firebase-link]:http://ozgur.github.io/python-firebase/
