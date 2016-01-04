from gi.repository import Gtk
from dialogCreatePassStore import DialogCreatePassStore

class BoxStart(Gtk.VButtonBox):

    def __init__(self, config):
        Gtk.VButtonBox.__init__(self)
        self.config = config
        #self.set_spacing(20)
        self.set_layout(Gtk.ButtonBoxStyle.CENTER)
        self.set_spacing(20)
        #Create Password Store
        self.btnCreatePassStore = Gtk.Button('Create Password Store')
        self.btnCreatePassStore.connect("clicked", self.btnCreatePassStore_clicked)
        self.pack_start(self.btnCreatePassStore, True, True, 0)

        #Select Password Store
        self.btnSelectPassStore = Gtk.Button('Select Password Store')
        self.btnSelectPassStore.connect("clicked", self.btnSelectPassStore_clicked)
        self.pack_start(self.btnSelectPassStore, True, True, 0)

        #Git Clone Password Store
        self.btnGitClonePassStore = Gtk.Button('Git Clone Password Store')
        self.btnGitClonePassStore.connect("clicked", self.btnGitClonePassStore_clicked)
        self.pack_start(self.btnGitClonePassStore, True, True, 0)

    def btnCreatePassStore_clicked(self, button):
        dialogCreatePassStore = DialogCreatePassStore(self.config)
        response = dialogCreatePassStore.run()

        if response == Gtk.ResponseType.OK:
            print("OK button clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")
        else:
            print("Dialog closed")

        dialogCreatePassStore.destroy()
        print('btnCreatePassStore_clicked')

    def btnSelectPassStore_clicked(self, button):
        print('btnSelectPassStore_clicked')

    def btnGitClonePassStore_clicked(self, button):
        print('btnGitClonePassStore_clicked')
