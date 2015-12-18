#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gpassconfig import GPassConfig
from mainPassUI import MainPassUI
#Starts the Application
def main():
    #reads in the config file
    passConfig = GPassConfig()
    #starts the UI
    win = MainPassUI(passConfig)
    win.show()
    Gtk.main()

if __name__ =='__main__':main()
