#!/usr/bin/env python3
import sys
import gi
gi.require_version('Gtk', '3.0')

from gPassApplication import GPassApplication

#Starts the Application
def main():
    app = GPassApplication()
    app.run(sys.argv)

if __name__ =='__main__':main()
