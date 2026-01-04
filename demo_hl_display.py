import board
import hl_display

# Connect to display
i2c = board.I2C()  # uses board.SCL and board.SDA
display_group = hl_display.display_init(i2c)

# Draw a label
text_area = hl_display.display_init_text(display_group)

print("Display setup using DisplayIO done.")

while True:
    pass
