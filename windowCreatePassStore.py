from gi.repository import Gtk, Gdk

class DialogCreatePassStore(Gtk.Dialog):

    #Constructor
    def __init__(self, parent):
        Gtk.Dialog.__init__(self)
        self.set_parent(parent)
        self.set_default_size(400, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_title("GPass Settings")
        self.vBox = Gtk.VBox(10)
        self.add(self.vBox)

        self.locationGroup = Gtk.Box(10)
        self.vBox.add(self.locationGroup)
        self.lblLocation = Gtk.Label("Select Folder:")
        self.locationGroup.add(self.lblLocation)
        self.txtLocation = Gtk.Entry()
        self.locationGroup.add(self.txtLocation)
        self.btnLocationSelect = Gtk.Button("Select")
        self.btnLocationSelect.clicked.connect(btnLocationSelect_Clicked)
        self.locationGroup.add(self.btnLocationSelect)

    def btnLocationSelect_Clicked(self, button):
        print 'btnLocationSelect_Clicked'

    #Show the Window
    def show(self):
        self.show_all()
