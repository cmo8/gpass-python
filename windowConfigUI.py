from gi.repository import Gtk, Gdk
from pypass import PyPass

class WindowConfigUI(Gtk.Window):

    #Constructor
    def __init__(self, config):
        Gtk.Window.__init__(self)
        self.set_default_size(700, 350);
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title("GPass Settings")



    #Show the Window
    def show(self):
        self.show_all()
