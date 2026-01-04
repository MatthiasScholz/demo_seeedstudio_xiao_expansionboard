# Connect to temperature and humidity sensor: AHT20
# NOTE Requires the following modules on the device within the `lib` folder:
# The modules are part of the Adafruit Library Bundle:
# .adafruit_ahtx0.mpy
import adafruit_ahtx0 as aht


def init(i2c):
    sensor_aht = aht.AHTx0(i2c)
    return sensor_aht


def str(sensor_aht):
    text_temp = "T: %0.1f" % sensor_aht.temperature
    text_humi = "H: %0.1f" % sensor_aht.relative_humidity
    return text_temp + " " + text_humi


def temp(sensor_aht):
    return sensor_aht.temperature


def humi(sensor_aht):
    return sensor_aht.humidity
