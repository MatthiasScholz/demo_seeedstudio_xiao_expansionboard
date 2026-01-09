# Demo Seeed Studio XIAO Expansion Board

- [Seeed Studio XIAO Expansion Board Base](https://www.seeedstudio.com/Seeeduino-XIAO-Expansion-board-p-4746.html)
- [Seeed Studio XIAO ESP32-S3](https://www.seeedstudio.com/Seeed-Studio-XIAO-ESP32S3-Pre-Soldered-p-6334.html)
- [Seeed Studio Grove AHT20 Environment Sensor](https://www.seeedstudio.com/Grove-AHT20-I2C-Industrial-grade-temperature-and-humidity-sensor-p-4497.html)
- [Seeed Studio Grove LED](https://www.seeedstudio.com/Grove-LED-Pack-p-4364.html) - NOTE: only used with 3.3V!

## Features

- Use Seeed Studio XIAO Expansion Board Base with ESP32-S3
- Examples using [CircuitPython](https://circuitpython.org)
- Very basic high level abstraction libraries for:
  - display usage for text output
  - connect to wifi
  - interact with MQTT broker (publish and subscribe)
  - read data from environment sensor via I2C
  - control an LED
- Uses [devenv](https://devenv.sh) for development environment setup

## References

### CircuitPython

- [Adafruit Library Bundle: Bundle for Version 10.x](https://circuitpython.org/libraries)
- [DisplayIO Introduction](https://learn.adafruit.com/circuitpython-display-support-using-displayio/introduction)
- [AHT20 + DisplayIO](https://docs.circuitpython.org/projects/ahtx0/en/latest/examples.html#displayio-simpletest)
- [LED](https://wiki.seeedstudio.com/Seeeduino-XIAO-Expansion-Board/#circuitpython-blink-example)
- [Wifi](https://learn.adafruit.com/networking-in-circuitpython/networking-with-the-wifi-module)
- [MQTT](https://learn.adafruit.com/networking-in-circuitpython/networking-with-the-wifi-module#using-mqtt-3177208)

### Emacs

- [REPL within Emacs](https://hadi.timachi.com/posts/micro_python_in_emacs)
