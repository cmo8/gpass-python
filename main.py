#!/usr/bin/env python
import sys
import gi
gi.require_version('Gtk', '3.0')

from appgpass import AppGPass

#Starts the Application
def main():
    app = AppGPass()
    app.run(sys.argv)

if __name__ =='__main__':main()
