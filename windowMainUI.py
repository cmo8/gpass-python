from gi.repository import Gtk, Gdk
from pypass import PyPass
from boxStart import BoxStart
from boxPassStore import BoxPassStore

class WindowMainUI(Gtk.ApplicationWindow):

    #Constructor
    def __init__(self, config):
        Gtk.ApplicationWindow.__init__(self)
        self.set_default_size(700, 350);
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title("GPass")

        #Create PyPass object
        self.gpass_config = config
        config_loaded = self.gpass_config.load_config()
        #self.startBox = BoxStart()

        print config_loaded
        self.gpass_config.config_test()
        if not config_loaded:
            self.startBox = BoxStart(self.gpass_config)
            self.add(self.startBox)
        else:
            self.pypas = PyPass(self.gpass_config)
            #Application Window
            self.passStoreBox = BoxPassStore(self.gpass_config)
            self.add(self.passStoreBox)

    #Show the Window
    def show(self):
        self.show_all()

    #bring window to the top
    def bringToTop(self):
        self.present()
