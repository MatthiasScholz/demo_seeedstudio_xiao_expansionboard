# Prints a message and drops into REPL
import sys

# Provides some insights on the hw and installed modules
import board

print(help("modules"))
print("dir board:")
print(dir(board))
# TODO how to know if the expansion board is correctly connected?

print("Hello world!")
sys.exit()
