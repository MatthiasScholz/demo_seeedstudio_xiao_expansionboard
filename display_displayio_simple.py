# SPDX-FileCopyrightText: 2025 MatthiasScholz
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid black
background and some white text.
"""

import board
import displayio

import terminalio
from i2cdisplaybus import I2CDisplayBus

# NOTE Requires the following modules on the device within the `lib` folder:
# The modules are part of the Adafruit Library Bundle:
# .adafruit_displayio_ssd1306.mpy
# .adafruit_display_text folder
import adafruit_displayio_ssd1306
from adafruit_display_text import label

displayio.release_displays()

# Use for I2C
i2c = board.I2C()  # uses board.SCL and board.SDA
display_bus = I2CDisplayBus(i2c, device_address=0x3C)

# Display configuration
WIDTH = 128
HEIGHT = 64

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Color management
COLOR_BACKGROUND = 0x000000  # Black
COLOR_FONT = 0xFFFFFF  # White

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = COLOR_BACKGROUND

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(
    terminalio.FONT, text=text, color=COLOR_FONT, x=28, y=HEIGHT // 2 - 1
)
splash.append(text_area)

print("Display setup using DisplayIO done.")

while True:
    pass
