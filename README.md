# Demo Seeed Studio XIAO Expansion Board

This repository contains the source code and development environment configuration for a [CircuitPython](https://circuitpython.org)-supported IoT device,
usable for a "smart switch" or environmental monitor.
It demonstrates the usage of Seeed Studio XIAO Expansion Board Base in combination with an ESP32-S3.

- [Seeed Studio XIAO Expansion Board Base](https://www.seeedstudio.com/Seeeduino-XIAO-Expansion-board-p-4746.html)
- [Seeed Studio XIAO ESP32-S3](https://www.seeedstudio.com/Seeed-Studio-XIAO-ESP32S3-Pre-Soldered-p-6334.html)
- [Seeed Studio Grove AHT20 Environment Sensor](https://www.seeedstudio.com/Grove-AHT20-I2C-Industrial-grade-temperature-and-humidity-sensor-p-4497.html)
- [Seeed Studio Grove LED](https://www.seeedstudio.com/Grove-LED-Pack-p-4364.html) - NOTE: only used with 3.3V!

The project is structured to provide a set of high-level, reusable libraries (`lib/hl_*.py`) that simplify common hardware and networking tasks.
These libraries act as wrappers around lower-level Adafruit drivers to make the main application code cleaner and more readable.

### Key Functionality

1.  **Connectivity:**
    *   Connects to a Wi-Fi network using credentials from a `settings.toml` file (`hl_wifi.py`).
    *   Connects to an MQTT broker (specifically configured for Adafruit IO) to send and receive data over the internet (`hl_mqtt.py`).

2.  **Sensing & Actuating:**
    *   Reads temperature and humidity from an AHT20 I2C sensor (`hl_environment_sensor.py`).
    *   Controls a digital LED, allowing it to be turned on or off (`hl_led.py`).
    *   Displays text and data on a small I2C OLED display (`hl_display.py`).

3.  **Application Logic (example: `demo_hl_mqtt.py`):**
    *   The main application initializes all hardware components.
    *   It periodically reads the temperature from the sensor and **publishes** it to an Adafruit IO MQTT feed.
    *   It **subscribes** to a different Adafruit IO feed to listen for commands (e.g., "ON" or "OFF").
    *   When a command is received, it controls the LED accordingly and updates the local display.

4.  **Development Environment (`devenv.nix`, `.envrc`):**
    *   The project uses [devenv](https://devenv.sh) and Nix to create a reproducible development environment. 
        This provides all necessary tools like `circup` (for managing CircuitPython libraries), `esptool` (for flashing firmware), and `thonny` (an IDE),
        ensuring a consistent setup for any developer working on the project.

## References

### Hardware

- [Seeed Studio XIAO Expansion Board Base: Pinout](https://wiki.seeedstudio.com/Seeeduino-XIAO-Expansion-Board/#pinout-diagram)

### CircuitPython

- [Adafruit Library Bundle: Bundle for Version 10.x](https://circuitpython.org/libraries)
- [DisplayIO Introduction](https://learn.adafruit.com/circuitpython-display-support-using-displayio/introduction)
- [AHT20 + DisplayIO](https://docs.circuitpython.org/projects/ahtx0/en/latest/examples.html#displayio-simpletest)
- [LED](https://wiki.seeedstudio.com/Seeeduino-XIAO-Expansion-Board/#circuitpython-blink-example)
- [Wifi](https://learn.adafruit.com/networking-in-circuitpython/networking-with-the-wifi-module)
- [MQTT](https://learn.adafruit.com/networking-in-circuitpython/networking-with-the-wifi-module#using-mqtt-3177208)

### Emacs

- [REPL within Emacs](https://hadi.timachi.com/posts/micro_python_in_emacs)
