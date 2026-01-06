# SPDX-FileCopyrightText: 2026 MatthiasScholz
import time
from os import getenv

# ----------
# Setup MQTT
import wifi

# NOTE Requires the following modules on the device within the `lib` folder:
# The modules are part of the Adafruit Library Bundle:
# .adafruit_connection_manager.mpy
# .adafruit_minimqtt
# .adafruit_ticks.mpy
import adafruit_connection_manager
import adafruit_minimqtt.adafruit_minimqtt as MQTT


def init():
    # Get WiFi details and Adafruit IO keys, ensure these are setup in settings.toml
    # (visit io.adafruit.com if you need to create an account, or if you need your Adafruit IO key.)
    broker_username = getenv("ADAFRUIT_AIO_USERNAME")
    broker_key = getenv("ADAFRUIT_AIO_KEY")
    broker = getenv("broker", "io.adafruit.com")

    # Create a socket pool and ssl_context
    pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
    ssl_context = adafruit_connection_manager.get_radio_ssl_context(wifi.radio)

    # If you need to use certificate/key pair authentication (e.g. X.509), you can load them in the
    # ssl context by uncommenting the lines below and adding the following keys to your settings.toml:
    # "device_cert_path" - Path to the Device Certificate
    # "device_key_path" - Path to the RSA Private Key
    # ssl_context.load_cert_chain(
    #     certfile=getenv("device_cert_path"), keyfile=getenv("device_key_path")
    # )

    # Set up a MiniMQTT Client
    mqtt_client = MQTT.MQTT(
        broker=broker,
        username=broker_username,
        password=broker_key,
        socket_pool=pool,
        ssl_context=ssl_context,
    )

    return mqtt_client
