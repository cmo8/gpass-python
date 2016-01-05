import os
from gi.repository import Gtk, Gdk

class DialogClonePassStoreRepo(Gtk.Dialog):

    #Constructor
    def __init__(self, parent, config):
        Gtk.Dialog.__init__(self, "Git Clone Password Store Repo", parent, 10,(Gtk.STOCK_OK, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
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

        #Repo to clone
        self.gitGroup = Gtk.Box(10)
        self.vlBox.add(self.gitGroup)
        self.lblGit = Gtk.Label("Remote Git Repo:")
        self.gitGroup.add(self.lblGit)
        self.txtRepo = Gtk.Entry()
        self.gitGroup.add(self.txtRepo)

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

    #Show the Window
    def show(self):
        self.show_all()
