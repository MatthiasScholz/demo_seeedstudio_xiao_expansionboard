# SPDX-FileCopyrightText: 2026 MatthiasScholz
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
from os import getenv

# ----------
# Connect to board
import board

i2c = board.I2C()

# -------------
# Setup display
import hl_display

display_group = hl_display.display_init(i2c)
text_area = hl_display.display_init_text(display_group)

# ------------------------
# Setup environment sensor
import hl_environment_sensor as hls

sensor = hls.init(i2c)

# ---------
# Setup LED
import hl_led

LED_PIN = board.D0  # depends on the connector
led = hl_led.init(LED_PIN)
hl_led.off(led)

# ------------------
# Connect to network
import hl_wifi

my_ip = hl_wifi.wifi_connect()


# ----------
# Setup MQTT
import hl_mqtt

# NOTE The current Adafruit IO Data Rate is
#      at most 1 request per second (or 60 requests within 60 seconds),
#      without an Adafruit IO+ Boost applied to your account.
UPDATE_RATE = 5  # every 5 seconds publish a new value

#### Feeds / MQTT topics ###
aio_username = getenv("ADAFRUIT_AIO_USERNAME")
feed_prefix = f"{aio_username}/feeds/camper-smart-switch"
# Setup a feed named for publishing to a feed
sensor_environment_feed = f"{feed_prefix}.sensor-environment"
# Setup a feed named for subscribing to changes
switch_led_feed = f"{feed_prefix}.switch-led"


# Implement MQTT Client interface
# Define callback methods which are called when events occur
def connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print(f"Connected to Adafruit IO! Listening for topic changes on {switch_led_feed}")
    # Subscribe to all changes on the onoff_feed.
    client.subscribe(switch_led_feed)


def disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from Adafruit IO!")


def message(client, topic, message):
    # This method is called when a topic the client is subscribed to
    # has a new message.
    msg = f"New message on topic {topic}: {message}"
    print(msg)
    text_area.text = f"{topic}:\n{message}"

    # Switch led based on the message
    if topic == switch_led_feed:
        if message == "ON":
            hl_led.on(led)
        if message == "OFF":
            hl_led.off(led)


# Set up a MiniMQTT Client
mqtt_client = hl_mqtt.init()

# Setup the callback methods above
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

# Connect the client to the MQTT broker.
print("Connecting to Adafruit IO...")
mqtt_client.connect()
text_area.text = "Connected to MQTT Broker"

while True:
    # Poll the message queue
    mqtt_client.loop(timeout=1)

    # Send a new message
    sensor_environment_val = hls.temp(sensor)
    print(f"Sending value: {sensor_environment_val}...")
    mqtt_client.publish(sensor_environment_feed, sensor_environment_val)
    print("Sent!")
    # TODO use a nicer approach to avoid blocking
    time.sleep(UPDATE_RATE)
