import WifiConnector
import utime
import sys
import server

WifiConnector.connect("wifi_config.json")
server.start()


flag = True
try:
    import loop
except Exception as e:
    sys.print_exception(e)
    flag = False

if flag:
    print('initialization completed! do loop...')
    while True:
        try:
            loop.loop()
        except Exception as e:
            sys.print_exception(e)
        utime.sleep(1)
