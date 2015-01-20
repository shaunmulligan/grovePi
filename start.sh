udevd &
#modprobe bcm2708_wdog
modprobe i2c-bcm2708
modprobe i2c-dev

python /app/firmware_version.py