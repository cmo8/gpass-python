from gi.repository import Gtk
from pypass import PyPass

class PopFolder:
    #Constructor
    def __init__(self, parent, btn, pypas):
        self.parent = parent
        self.pypas = pypas
        self.btn = btn
        self.folder = Gtk.Entry()
        self.popFolder = self.create_folder_popover_menu()

    #Button Create Folder click event
    def create_folder_clicked(self, button):
        if not self.folder.get_text() == "":
            self.pypas.createFolder(self.folder.get_text(), self.parent.get_pass_path())
            self.parent.repack_buttons()
            self.popFolder.hide()
        else:
            print "No new folder entered"

    #Button Cancel Folder click event
    def cancel_clicked(self, button, name):
        print "Cancel Delete"
        self.popFolder.hide()

    #Create the Delete poperover confirm menu
    def create_folder_popover_menu(self):
        #Creating a popover
        popover = Gtk.Popover.new(self.btn)

        hbox = Gtk.VBox(10)
        popover.add(hbox)

        fbox = Gtk.Box(10)
        hbox.add(fbox)
        label = Gtk.Label("Folder Name:")
        fbox.pack_start(label, False, False, 0)

        fbox.pack_start(self.folder, False, False, 0)

        button = Gtk.Button("Create")
        button.connect("clicked", self.create_folder_clicked)
        hbox.pack_start(button, False, False, 0)
        return popover

    #Show the menu
    def show(self):
        self.popFolder.show_all()
