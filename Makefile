run:
	python3 gpass/main.py

setup:
	python3 -m pip install gitpython
	python3 -m pip install python-gnupg
	#python3 -m pip install gittle
	#python3 -m pip install nose

fedora:
	sudo dnf install redhat-rpm-config

ubuntu:
	sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
