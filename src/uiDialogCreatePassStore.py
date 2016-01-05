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
        self.set_default_size(400, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.box = self.get_content_area()
        self.vlBox = Gtk.Grid()
        self.box.add(self.vlBox)
        self.vlBox.set_row_spacing(20)
        self.vlBox.set_column_spacing(20)
        self.vlBox.set_row_homogeneous(20)
        self.vlBox.set_column_homogeneous(20)

        #Select Root parent folder
        self.lblLocation = Gtk.Label("Select Folder:")
        self.vlBox.add(self.lblLocation)
        self.txtLocation = Gtk.Entry()
        self.txtLocation.set_text(self.config.password_store);
        self.vlBox.attach(self.txtLocation, 1, 0, 3, 1)
        self.btnLocationSelect = Gtk.Button("Select")
        self.btnLocationSelect.connect("clicked", self.btnLocationSelect_Clicked)
        self.vlBox.attach_next_to(self.btnLocationSelect, self.txtLocation, Gtk.PositionType.RIGHT, 1, 1)

        self.lblKeys = Gtk.Label("GPG Key:")
        self.vlBox.attach_next_to(self.lblKeys, self.lblLocation, Gtk.PositionType.BOTTOM, 1, 1)
        if os.path.isdir(self.config.gpghome) and len(keys) > 0:
            name_store = Gtk.ListStore(str, str)
            for key in keys:
                #print(key, "=>", keys[key])
                name_store.append([key, keys[key]])
            self.listBoxGPGkey = Gtk.ComboBox.new_with_model_and_entry(name_store)
            self.listBoxGPGkey.connect("changed", self.listBoxGPGkey_changed)
            self.listBoxGPGkey.set_entry_text_column(1)
            self.vlBox.attach_next_to(self.listBoxGPGkey, self.lblKeys, Gtk.PositionType.RIGHT, 3, 1)
        else:
            self.gen_key = True
            #Key name folder
            self.createGPGkey = BoxCreateGPGKey()
            self.vlBox.attach_next_to(self.createGPGkey, self.lblKeys, Gtk.PositionType.RIGHT, 3, 1)
        
        #Git Group
        self.lblGit = Gtk.Label("Set up Git:")
        self.vlBox.attach_next_to(self.lblGit, self.lblKeys, Gtk.PositionType.BOTTOM, 1, 1)
        self.checkBoxGit = Gtk.CheckButton()
        self.vlBox.attach_next_to(self.checkBoxGit, self.lblGit, Gtk.PositionType.RIGHT, 3, 1)

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
