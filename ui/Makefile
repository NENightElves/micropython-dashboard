all: build copy

build:
	yarn build

copy:
	cd ..; \
	rm -r ./micropython/www; \
	cp -r ./ui/dist/build/h5 ./micropython/www;
