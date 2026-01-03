# SPDX-FileCopyrightText: 2025 MatthiasScholz
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid black
background and some white text.
"""

# General python imports
import time

# Microcontroller environment specific imports
import board
import displayio

import terminalio
from i2cdisplaybus import I2CDisplayBus


# Hardware specific imports
# NOTE Requires the following modules on the device within the `lib` folder:
# The modules are part of the Adafruit Library Bundle:
# .adafruit_displayio_ssd1306.mpy
# .adafruit_display_text folder
import adafruit_displayio_ssd1306

# Display configuration (monochrome OLED)
WIDTH = 128
HEIGHT = 64
# Color management
# NOTE monochrome OLED display
COLOR_BACKGROUND = 0x000000  # Black
COLOR_FONT = 0xFFFFFF  # White
DISPLAY_UPDATE_RATE = 2  # Update display in seconds

from adafruit_display_text import label

# Start clean
displayio.release_displays()

# Use for I2C bus for display and some sensors
i2c = board.I2C()  # uses board.SCL and board.SDA

# Connect to temperature and humidity sensor: AHT20
# NOTE Requires the following modules on the device within the `lib` folder:
# The modules are part of the Adafruit Library Bundle:
# .adafruit_ahtx0.mpy
import adafruit_ahtx0 as aht

sensor_aht = aht.AHTx0(i2c)


# Connect to display
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)


# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = COLOR_BACKGROUND

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a label
text = "Hello from Camper Smart Switch!"
text_area = label.Label(
    terminalio.FONT, text=text, color=COLOR_FONT, x=28, y=HEIGHT // 2 - 1
)
splash.append(text_area)

# Display welcome message for two seconds
time.sleep(2)

while True:
    # Draw a sensor reading
    text_temp = "T: %0.1f" % sensor_aht.temperature
    text_humi = "H: %0.1f" % sensor_aht.relative_humidity
    text_area.text = text_temp + " " + text_humi

    # Update the text continuously
    time.sleep(DISPLAY_UPDATE_RATE)
