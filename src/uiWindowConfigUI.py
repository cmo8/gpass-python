from gi.repository import Gtk, Gdk
from gPassGPG import GPassGPG
from uiBoxCreateGPGKey import BoxCreateGPGKey

class WindowConfigUI(Gtk.Window):

    #Constructor
    def __init__(self, config):
        Gtk.Window.__init__(self)
        self.config = config
        self.gpg = GPassGPG(self.config.gpgbinary, self.config.gpghome)
        self.set_default_size(700, 350);
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title("GPass Settings")

        self.vbox = Gtk.VBox(10)
        self.add(self.vbox)
        self.btnCreateGPGKey = Gtk.Button('Create GPG Key')
        self.btnCreateGPGKey.connect("clicked", self.btnCreateGPGKey_clicked)
        self.vbox.pack_start(self.btnCreateGPGKey, True, True, 0)

    def btnCreateGPGKey_clicked(self, button):
        dialogCreateGPGKey = Gtk.Dialog("Create GPG Key", self, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        dialogCreateGPGKey.set_default_size(250, 300)
        vbox  = dialogCreateGPGKey.get_content_area()
        boxCreateGPGKey = BoxCreateGPGKey()
        vbox.add(boxCreateGPGKey)
        response = dialogCreateGPGKey.run()

        if response == Gtk.ResponseType.OK:
            real_name = boxCreateGPGKey.get_real_name()
            email = boxCreateGPGKey.get_email()
            password = boxCreateGPGKey.get_password()
            passwordc = boxCreateGPGKey.get_confirmation()
            if real_name != "" and email != "" and password != "" and passwordc != "" and password == passwordc:
                print("Real Name:", real_name)
                print("Email:", email)
                self.gpg.generate_key(real_name, email, password)
            print("OK button clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")
        else:
            print("Dialog closed")
        dialogCreateGPGKey.destroy()

    #Show the Window
    def show(self):
        self.show_all()
