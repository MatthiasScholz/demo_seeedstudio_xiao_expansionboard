import time
import board
from digitalio import DigitalInOut, Direction, Pull

print(dir(board))

# Pins
led = DigitalInOut(board.D0)
led.direction = Direction.OUTPUT
button = DigitalInOut(board.D1)
button.direction = Direction.INPUT
# NOTE There’s an easy way to prevent an input from floating
# by using special built-in pull-up or pull-down resistors
# available on most development board digital I/O pins.
# You can turn on a pull-up resistor that will bring
# the digital input up to a high digital logic level
# if nothing is connected to it.
# This prevents the input from floating and
# will instead read a high digital logic level.
# NOTE Set the input to have an internal pull-up resistor
# that reads a high digital logic level when nothing else is connected.
button.pull = Pull.UP

# Turn LED off on button hold
update_rate = 2  # in secs
led.value = False
while True:
    if button.value:
        led.value = True
    else:
        led.value = False
    time.sleep(update_rate)
