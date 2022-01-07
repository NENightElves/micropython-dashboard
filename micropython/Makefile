libs = microWebSrv.py microWebSocket.py microWebSrv.py
programs = main.py WifiConnector.py loop.py
server = server.py
web = www
config= wifi_config.json server_config.json
PORT = /dev/ttyUSB0


all: libs programs server web config

libs:
	for i in $(libs); do ampy -p $(PORT) put $$i; done

programs:
	for i in $(programs); do ampy -p $(PORT) put $$i; done

server:
	for i in $(server); do ampy -p $(PORT) put $$i; done

web:
	for i in $(web); do ampy -p $(PORT) put $$i; done

config:
	for i in $(config); do ampy -p $(PORT) put $$i; done