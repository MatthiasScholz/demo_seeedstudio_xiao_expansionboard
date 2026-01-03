# Import all board pins.
import busio
import board

# NOTE Requires the following modules on the device within the `lib` folder:
# The modules are part of the Adafruit Library Bundle:
# .adafruit_ssd1306.mpy
# .adafruit_framebuf.mpy
import adafruit_ssd1306

# Create the SSD1306 OLED class.
display_width = 128
display_height = 64

# Scan for display
# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(display_width, display_height, i2c)
# You can change the I2C address with an addr parameter:
# display = adafruit_ssd1306.SSD1306_I2C(display_width, display_height, i2c, addr=0x31)

# Clear the display.
# Fills display with black pixels clearing it
# Always call show after changing pixels to make the display update visible!
display.fill(0)
display.show()

# Set some pixels
# Corner 1
display.pixel(0, 0, 1)
# Middle
# .Set a pixel in the middle 64, 16 position.
display.pixel(int(display_width / 2), int(display_height / 2), 1)
# Corner 4
display.pixel(display_width - 1, display_height - 1, 1)
display.show()

print("Display setup done.")
