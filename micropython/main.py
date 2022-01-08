import WifiConnector
import server

flag = True

try:
    import loop
except Exception as e:
    print(e)
    flag = False

WifiConnector.connect("wifi_config.json")

server.start()

if flag:
    print('initialization completed! do loop...')
    while True:
        try:
            loop.loop()
        except Exception as e:
            print(e)
