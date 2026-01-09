import hl_wifi

networks = hl_wifi.wifi_scan(verbose=True)
my_ip = hl_wifi.wifi_connect(verbose=True)
