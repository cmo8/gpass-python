from gi.repository import Gtk
from pypass import PyPass

class PopAddItem:

    #ConstructorPopAddItem
    def __init__(self, parent, btn, pypas, data):
        self.parent = parent
        self.btn = btn
        self.pypas = pypas
        self.data = data
        self.txtKey = Gtk.Entry()
        self.txtValue = Gtk.Entry()
        self.popAddItem = self.create_additem_popover_menu()

    #Button Yes click event
    def on_add_item_button_click(self, button):
        key = self.txtKey.get_text()
        value = self.txtValue.get_text()
        self.data += key.lower() + ': ' + value + '\n'
        self.pypas.insert(self.parent.get_pass_path(), self.data)
        print "Add Item"
        self.parent.clear_account_info(False)
        self.parent.displayAccount(self.parent.get_pass_path())
        self.popAddItem.hide()

    #Create the Add Item poperover confirm menu
    def create_additem_popover_menu(self):
        #Creating a popover
        popover = Gtk.Popover.new(self.btn)

        hbox = Gtk.VBox(10)
        popover.add(hbox)

        label = Gtk.Label("Add Item Key => Value")
        hbox.pack_start(label, False, False, 0)

        hboxkey = Gtk.Box(10)
        hbox.pack_start(hboxkey, False, False, 0)
        labelKey = Gtk.Label("Key: ")
        hboxkey.pack_start(labelKey, False, False, 0)
        hboxkey.pack_start(self.txtKey, False, False, 0)

        hboxvalue = Gtk.Box(10)
        hbox.pack_start(hboxvalue, False, False, 0)
        labelValue = Gtk.Label("Value: ")
        hboxvalue.pack_start(labelValue, False, False, 0)
        hboxvalue.pack_start(self.txtValue, False, False, 0)

        button = Gtk.ToggleButton("+ Add")
        button.connect("clicked", self.on_add_item_button_click)
        hbox.pack_start(button, False, False, 0)
        return popover


    #Show the menu
    def show(self):
        self.popAddItem.show_all()

