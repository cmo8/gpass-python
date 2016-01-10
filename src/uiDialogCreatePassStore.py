import os
from gi.repository import Gtk, Gdk
from uiBoxCreateGPGKey import BoxCreateGPGKey

class DialogCreatePassStore(Gtk.Dialog):
    #Constructor
    def __init__(self, parent, keys):
        Gtk.Dialog.__init__(self, "Create Password Store", parent, 10,(Gtk.STOCK_OK, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        self.gen_key = False
        self.parent = parent
        self.config = self.parent.config
        self.selected_key = None
        self.set_default_size(250, 250)
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
        self.txtLocation.set_text(self.config.password_store);
        self.locationGroup.add(self.txtLocation)
        self.btnLocationSelect = Gtk.Button("Select")
        self.btnLocationSelect.connect("clicked", self.btnLocationSelect_Clicked)
        self.locationGroup.pack_start(self.btnLocationSelect, False, False, 10)

        self.gpgkeyGroup = Gtk.VBox(10)
        self.vlBox.add(self.gpgkeyGroup)
        if os.path.isdir(self.config.gpghome) and len(keys) > 0:
            self.keysGroup = Gtk.Box(10)
            self.gpgkeyGroup.add(self.keysGroup)
            self.lblKeys = Gtk.Label("GPG Key:")
            self.keysGroup.add(self.lblKeys)
            name_store = Gtk.ListStore(str, str)
            for key in keys:
                #print(key, "=>", keys[key])
                name_store.append([key, keys[key]])
            self.listBoxGPGkey = Gtk.ComboBox.new_with_model_and_entry(name_store)
            self.listBoxGPGkey.connect("changed", self.listBoxGPGkey_changed)
            self.listBoxGPGkey.set_entry_text_column(1)
            self.keysGroup.add(self.listBoxGPGkey)
        else:
            self.gen_key = True
            #Key name folder
            self.createGPGkey = Gtk.BoxCreateGPGKey()
            self.gpgkeyGroup.add(self.createGPGkey)
        self.show_all()

    def btnLocationSelect_Clicked(self, button):
        filechooserdialog = Gtk.FileChooserDialog(self, self.parent, title="Open Password Store", buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        filechooserdialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        email_filter = Gtk.FileFilter()
        email_filter.set_name("Folder")
        email_filter.add_pattern("*")  # whats the pattern for a folder
        filechooserdialog.add_filter(email_filter)
        response = filechooserdialog.run()
        if response == Gtk.ResponseType.OK:
            self.txtLocation.set_text(filechooserdialog.get_filename())
        filechooserdialog.destroy()

#    def btnCreateGPGkey_Clicked(self, button):
#        real_name = self.txtKeyName.get_text()
#        email = self.txtEmail.get_text()
#        password = self.txtPassword.get_text()
#        passwordc = self.txtPasswordC.get_text()
#        if real_name != "" and email != "" and password != "" and passwordc != "" and password == passwordc:
#            print("Real Name:", real_name)
#            print("Email:", email)
#            self.gpg.generate_key(real_name, email, password)
#
#        else:
#            print("Can NOT Generate Key!!")

    def listBoxGPGkey_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]
            print("Selected: ID=%s, name=%s" % (row_id, name))
            self.selected_key = name
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())

    #Show the Window
    def show(self):
        self.show_all()
