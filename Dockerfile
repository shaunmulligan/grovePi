FROM resin/rpi-raspbian:wheezy-2014-01-15

# Install Python.
RUN apt-get update
RUN apt-get install -y python python-dev python-pip git libi2c-dev python-serial python-rpi.gpio i2c-tools python-smbus 

RUN git clone git://git.drogon.net/wiringPi && cd wiringPi && ./build && echo "wiringPi Installed"
RUN echo i2c-dev >> /etc/modules
RUN echo i2c-bcm2708 >> /etc/modules
RUN echo spi-dev >> /etc/modules

COPY . /app

CMD ["python", "/app/demo.py"]

