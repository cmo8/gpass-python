from gi.repository import Gtk, Gdk
from gPass import GPass
from uiBoxStart import BoxStart
from uiBoxPassStore import BoxPassStore
from uiBoxConfig import BoxConfig

class WindowMainUI(Gtk.ApplicationWindow):

    #Constructor
    def __init__(self, config):
        Gtk.ApplicationWindow.__init__(self)
        self.set_default_size(700, 350);
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title("GPass")

        #Create PyPass object
        self.config = config
        config_loaded = self.config.load_config()
        self.gpass = GPass(self.config)
        self.currentBox = None
        self.pastBox = None
        self.startBox = None
        self.passStoreBox = None
        self.configBox = None
        print(config_loaded)
        self.config.config_test()
        if not config_loaded:
            self.startBox = BoxStart(self)
            self.add(self.startBox)
            self.currentBox = self.startBox
        else:
            #Application Window
            self.passStoreBox = BoxPassStore(self)
            self.add(self.passStoreBox)
            self.currentBox = self.passStoreBox

    #Show the Window
    def show(self):
        self.show_all()

    #bring window to the top
    def bringToTop(self):
        self.present()

    def setPassStoreView(self):
        self.remove(self.currentBox)
        if self.passStoreBox == None:
            self.passStoreBox = BoxPassStore(self)
        self.add(self.passStoreBox)
        self.currentBox = self.passStoreBox
        self.show_all()

    def setStartUpView(self):
        self.remove(self.currentBox)
        if self.startBox == None:
            self.startBox = BoxStart(self)
        self.add(self.startBox)
        self.currentBox = self.startBox
        self.show_all()

    def setConfigView(self):
        self.pastBox = self.currentBox
        self.remove(self.currentBox)
        if self.configBox == None:
            self.configBox = BoxConfig(self)
        self.add(self.configBox)
        self.currentBox = self.configBox
        self.show_all()

    def setPastView(self):
        self.remove(self.currentBox)
        self.add(self.pastBox)
        self.pastBox = None
        self.show_all()
