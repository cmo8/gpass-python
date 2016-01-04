import os
from gi.repository import Gtk, Gdk
from gpgkey import GPGkey

class DialogCreatePassStore(Gtk.Dialog):

    #Constructor
    def __init__(self, config):
        Gtk.Dialog.__init__(self, title="Create Password Store", buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        #self.set_parent(parent)
        self.config = config
        self.set_default_size(400, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.box = self.get_content_area()
        self.vlBox = Gtk.VBox(10)
        self.box.add(self.vlBox)

        #Select Root parent folder
        self.locationGroup = Gtk.Box(10)
        self.vlBox.add(self.locationGroup)
        self.lblLocation = Gtk.Label("Select Folder:")
        self.locationGroup.add(self.lblLocation)
        self.txtLocation = Gtk.Entry()
        self.locationGroup.add(self.txtLocation)
        self.btnLocationSelect = Gtk.Button("Select")
        self.btnLocationSelect.connect("clicked", self.btnLocationSelect_Clicked)
        self.locationGroup.add(self.btnLocationSelect)

        self.gpgkeyGroup = Gtk.Box(10)
        self.vlBox.add(self.gpgkeyGroup)
        #GPG section
        if os.path.isdir(self.config.gpghome):
            self.gpg = GPGkey(self.config.gpgbinary, self.config.gpghome)
            self.gpg.list_public_keys()
            keys = self.gpg.list_keys()
            self.lblKeys = Gtk.Label("GPG Key:")
            self.gpgkeyGroup.add(self.lblKeys)
            name_store = Gtk.ListStore(str, str)
            for key in keys:
                #print key, "=>", keys[key]
                name_store.append([key, keys[key]])
            self.listBoxGPGkey = Gtk.ComboBox.new_with_model_and_entry(name_store)
            self.listBoxGPGkey.connect("changed", self.listBoxGPGkey_changed)
            self.listBoxGPGkey.set_entry_text_column(1)
            self.gpgkeyGroup.add(self.listBoxGPGkey)
        else:
            self.btnCreateGPGhome = Gtk.Button("Create GPG Key")
            self.btnCreateGPGhome.connect("clicked", self.btnCreateGPGhome_Clicked)
            self.gpgkeyGroup.add(self.btnCreateGPGhome)
            print "No: " + self.config.gpgbinary


        self.show_all()

    def btnLocationSelect_Clicked(self, button):
        filechooserdialog = Gtk.FileChooserDialog(self, title="Open Password Store", buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        filechooserdialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        email_filter = Gtk.FileFilter()
        email_filter.set_name("Folder")
        email_filter.add_pattern("*")  # whats the pattern for a folder
        filechooserdialog.add_filter(email_filter)
        response = filechooserdialog.run()
        if response == Gtk.ResponseType.OK:
            self.txtLocation.set_text(filechooserdialog.get_filename())
        filechooserdialog.destroy()

    def btnCreateGPGhome_Clicked(self, button):
        #self.gpgkeyGroup =
        print "btnCreateGPGhome_Clicked"

    def listBoxGPGkey_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]
            print("Selected: ID=%s, name=%s" % (row_id, name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())

    #Show the Window
    def show(self):
        self.show_all()
