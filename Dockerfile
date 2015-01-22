FROM resin/rpi-raspbian:wheezy-2015-01-15

# Install Python.
RUN apt-get update
RUN apt-get install -y sudo python python-dev python-pip git libi2c-dev python-serial i2c-tools python-smbus 

RUN git clone https://github.com/WiringPi/WiringPi.git && cd WiringPi && ./build && echo "wiringPi Installed"
RUN pip install RPi.GPIO

COPY . /app

CMD ["bash", "/app/start.sh"]

