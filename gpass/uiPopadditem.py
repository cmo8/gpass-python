from gi.repository import Gtk
#from gpasss import PyPass

class PopAddItem:

    #ConstructorPopAddItem
    def __init__(self, parent, btn, data):
        self.parent = parent
        self.gpass = self.parent.gpass
        self.btn = btn
        self.data = data
        self.txtKey = Gtk.Entry()
        self.txtValue = Gtk.Entry()
        self.popAddItem = self.create_additem_popover_menu()

    #Button Yes click event
    def on_add_item_button_click(self, button):
        key = self.txtKey.get_text()
        value = self.txtValue.get_text()
        if key != '' and value != '':
            self.data += key.lower() + ': ' + value + '\n'
            self.gpass.insert(self.parent.get_pass_path(), self.data)
            self.parent.new_status("Added:" + key + ": " + value)
            #print("Add Item")
            self.parent.clear_account_info(False)
            self.parent.displayAccount(self.parent.get_pass_path())
        else:
            self.parent.clear_status()
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
        self.parent.clear_status()
        self.popAddItem.show_all()

