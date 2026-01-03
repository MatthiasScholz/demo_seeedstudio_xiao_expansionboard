# NOTE LED is 5V, but max voltage is 3.3 on the XIAO expension board
#      Hence LED is very dimmed

import time
import board
from digitalio import DigitalInOut, Direction

# LED Pin
pin = board.DO  # depends on the connector
update_rate = 2  # in secs

led = DigitalInOut(pin)
led.direction = Direction.OUTPUT

# Let the LED blink
while True:
    led.value = True
    time.sleep(update_rate)
    led.value = False
    time.sleep(update_rate)
