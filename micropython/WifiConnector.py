import json
import network
import utime


def connect(filename):
    config = None
    try:
        with open(filename, 'r') as f:
            config = json.loads(f.read())
    except OSError:
        pass
    if not config or 'essid' not in config or 'password' not in config:
        print('connection failed!')
        start_ap()
        return
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        if config['static']:
            wlan.ifconfig((config['static']['ip'], config['static']['subnet'], config['static']['gateway'], config['static']['dns']))
        wlan.connect(config['essid'], config['password'])
        i = 0
        while i < 10 and not wlan.isconnected():
            i += 1
            utime.sleep(1)
    if not wlan.isconnected():
        wlan.active(False)
        print('connection failed!')
        start_ap()
        return
    print('network config:', wlan.ifconfig())


def start_ap():
    essid = 'esp32'
    password = '12345678'
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=essid, password=password, authmode=4)
    print('ap config: %s, %s' % (essid, password))
    print('ap config:', ap.ifconfig())
