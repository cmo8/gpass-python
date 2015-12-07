#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from passui import PassUI

def main():
    win = PassUI()
    win.show()
    Gtk.main()

if __name__ =='__main__':main()
