import board
from digitalio import DigitalInOut, Direction

# LED Pin
DEFAULT_PIN = board.D0  # depends on the connector


def init(pin=DEFAULT_PIN):
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    return led


def on(led):
    led.value = True


def off(led):
    led.value = False
