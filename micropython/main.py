import WifiConnector
import server
import loop

WifiConnector.connect("wifi_config.json")

server.start()

print('initialization completed! do loop...')
while True:
    try:
        loop.loop()
    except Exception as e:
        print(e)
        pass
