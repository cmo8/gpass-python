from gi.repository import Gtk, Gdk
from pypass import PyPass

class WindowConfigUI(Gtk.Window):

    #Constructor
    def __init__(self, config):
        Gtk.Window.__init__(self)
        self.set_default_size(700, 350);
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title("GPass Settings")

        self.vbox = Gtk.VBox(10)
        self.add(self.vbox)
        self.btnCreateGPGKey = Gtk.Button('Create GPG Key')
        self.btnCreateGPGKey.connect("clicked", self.btnCreateGPGKey_clicked)
        self.vbox.pack_start(self.btnCreateGPGKey, True, True, 0)

    def btnCreateGPGKey_clicked(self):
        dialogClonePassStoreRepo = DialogClonePassStoreRepo(self.parent, self.config)
        response = dialogClonePassStoreRepo.run()

        if response == Gtk.ResponseType.OK:
            location = dialogClonePassStoreRepo.txtLocation.get_text()
            repo = dialogClonePassStoreRepo.txtRepo.get_text()
            print("Location:", location)
            print("Repo:", repo)
            print("OK button clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")
        else:
            print("Dialog closed")
        dialogClonePassStoreRepo.destroy()

    #Show the Window
    def show(self):
        self.show_all()
