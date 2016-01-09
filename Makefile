APP=gpass
HOME=/home/cmo
BIN=/usr/bin/gpass
BASE=/usr/share/$(APP)
LIB=$(BASE)/lib/
IMAGES=$(BASE)/images/
LOCALE=/usr/share
MAIN=main.py

run:
	python3 $(MAIN)

testh:
	mkdir -p $(HOME)/usr
	mkdir -p $(HOME)/usr/bin
	mkdir -p $(HOME)/usr/share
	mkdir -p $(HOME)$(BASE)
	mkdir -p $(HOME)$(LIB)
	mkdir -p $(HOME)$(IMAGES)
	cp *.py $(HOME)$(LIB)
	cp *.glade $(HOME)$(LIB)
	rm -f $(HOME)$(BIN)
	ln -s $(HOME)$(LIB)$(MAIN) $(HOME)$(BIN)

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


