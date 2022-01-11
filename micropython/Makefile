slibs = microWebSrv.py microWebSocket.py microWebTemplate.py
libs = microWebSrv.mpy microWebSocket.mpy microWebTemplate.mpy
sprograms = WifiConnector.py
programs = WifiConnector.mpy
sserver = server.py
server = server.mpy
main = main.py
web = www
uprogram = loop.py
config= wifi_config.json server_config.json
PORT = /dev/ttyUSB0


all: compile_all main libs programs server config web

main: $(main)
	for i in $(main); do ampy -p $(PORT) put $$i; done

uprogram: $(uprogram)
	for i in $(uprogram); do ampy -p $(PORT) put $$i; done

libs: $(libs)
	for i in $(libs); do ampy -p $(PORT) put $$i; done

programs: $(programs)
	for i in $(programs); do ampy -p $(PORT) put $$i; done

server: $(server)
	for i in $(server); do ampy -p $(PORT) put $$i; done

config: $(config)
	for i in $(config); do ampy -p $(PORT) put $$i; done

web: $(web)
	for i in $(web); do ampy -p $(PORT) put $$i; done

compile_all: compile_libs compile_programs compile_server

compile_libs: $(libs)

compile_programs: $(programs)

compile_server: $(server)

$(libs): $(slibs)
	for i in $(slibs); do mpy-cross -O3 $$i; done

$(programs): $(sprograms)
	for i in $(sprograms); do mpy-cross -O3 $$i; done

$(server): $(sserver)
	for i in $(sserver); do mpy-cross -O3 $$i; done

clean:
	rm $(libs) $(programs) $(server)
