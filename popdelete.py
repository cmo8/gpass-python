from gi.repository import Gtk
from pypass import PyPass

class PopDelete:
    #Constructor
    def __init__(self, parent, btn, pypas):
        self.parent = parent
        self.pypas = pypas
        self.btn = btn
        self.popDelete = self.create_delete_popover_menu()

    #Button Yes click event
    def on_delete_yes_button_toggled(self, button, name):
        self.pypas.delete(self.parent.get_pass_path())
        self.parent.repack_buttons()
        print "Yes Delete"
        self.popDelete.hide()

    #Button No click event
    def on_delete_no_button_toggled(self, button, name):
        print "Cancel Delete"
        self.popDelete.hide()

    #Create the Delete poperover confirm menu
    def create_delete_popover_menu(self):
        #Creating a popover
        popover = Gtk.Popover.new(self.btn)

        hbox = Gtk.VBox(10)
        popover.add(hbox)

        label = Gtk.Label("Are you sure?")
        hbox.add(label)

        hboxtwo = Gtk.Box(10)
        hbox.add(hboxtwo)

        button = Gtk.ToggleButton("Yes")
        button.connect("toggled", self.on_delete_yes_button_toggled, "1")
        hboxtwo.pack_start(button, False, False, 0)

        button = Gtk.ToggleButton("No")
        button.connect("toggled", self.on_delete_no_button_toggled, "2")
        hboxtwo.pack_start(button, False, False, 0)
        return popover

    #Show the menu
    def show(self):
        self.popDelete.show_all()
