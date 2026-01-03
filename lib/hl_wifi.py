import wifi
import os


def wifi_scan(verbose=False):
    """
    Create a wifi network overview.
    """
    # .Search for wifi
    networks = []
    for network in wifi.radio.start_scanning_networks():
        networks.append(network)
    wifi.radio.stop_scanning_networks()

    # .List wifi networks
    networks = sorted(networks, key=lambda net: net.rssi, reverse=True)

    if verbose:
        for network in networks:
            print("ssid:", network.ssid, "rssi:", network.rssi)

    return networks


def wifi_connect(verbose=False):
    """
    Connect to a specific network
    """

    # Reading wifi configuration from `settings.toml`
    wifi_ssid = os.getenv("CIRCUITPY_WIFI_SSID")
    wifi_pwd = os.getenv("CIRCUITPY_WIFI_PASSWORD")

    if verbose:
        print("connecting...")

    wifi.radio.connect(ssid=wifi_ssid, password=wifi_pwd)
    if verbose:
        print("my IP addr:", wifi.radio.ipv4_address)

    return wifi.radio.ipv4_address
