import displayio

import terminalio
from i2cdisplaybus import I2CDisplayBus


# NOTE Requires the following modules on the device within the `lib` folder:
# The modules are part of the Adafruit Library Bundle:
# .adafruit_displayio_ssd1306.mpy
# .adafruit_display_text folder
import adafruit_displayio_ssd1306
from adafruit_display_text import label

# Display configuration
HL_DISPLAY_WIDTH = 128
HL_DISPLAY_HEIGHT = 64

# Color management
HL_DISPLAY_COLOR_BACKGROUND = 0x000000  # Black
HL_DISPLAY_COLOR_FONT = 0xFFFFFF  # White


def display_init(i2c, verbose=False):
    """
    Connects to the display and provides a main display group with a background.
    """
    displayio.release_displays()

    # Use for I2C
    display_bus = I2CDisplayBus(i2c, device_address=0x3C)

    display = adafruit_displayio_ssd1306.SSD1306(
        display_bus, width=HL_DISPLAY_WIDTH, height=HL_DISPLAY_HEIGHT
    )

    # Make the display context
    dg = displayio.Group()
    display.root_group = dg

    color_bitmap = displayio.Bitmap(HL_DISPLAY_WIDTH, HL_DISPLAY_HEIGHT, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = HL_DISPLAY_COLOR_BACKGROUND

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    dg.append(bg_sprite)

    return dg


def display_init_text(
    display_group, text="Hello World!", pos_x=28, pos_y=HL_DISPLAY_HEIGHT // 2 - 1
):
    # Create a label with initial text
    text_area = label.Label(
        terminalio.FONT,
        text=text,
        color=HL_DISPLAY_COLOR_FONT,
        x=pos_x,
        y=pos_y,  # DISPLAY_HEIGHT // 2 - 1,
    )
    display_group.append(text_area)
    return text_area
