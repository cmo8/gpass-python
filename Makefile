APP=gpass
HOME=/home/cmo
BIN=/usr/bin/gpass
BASE=/usr/share/$(APP)
LIB=$(BASE)/lib/
IMAGES=$(BASE)/images/
LOCALE=/usr/share
MAIN=main.py

run:
	python3 src/$(MAIN)

dev:
	python3 src/test_gpass.py
	python3 src/test_gpassgpg.py

install:
	mkdir -p $(BASE)
	mkdir -p $(LIB)
	mkdir -p $(IMAGES)
	cp *.py $(LIB)
	cp *.glade $(LIB)
	rm -f $(BIN)
	ln -s $(LIB)$(MAIN) $(BIN)

uninstall:
	rm -f $(BIN)
	rm -f $(LIB)/*
	rm -f $(IMAGES)/*
	rmdir $(LIB)
	rmdir $(IMAGES)
	rmdir $(BASE)

setup:
	python3 -m pip install gitpython
	python3 -m pip install python-gnupg
	python3 -m pip install gittle
	python3 -m pip install nose

fedora:
	sudo dnf install redhat-rpm-config