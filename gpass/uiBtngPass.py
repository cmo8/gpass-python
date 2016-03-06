from gi.repository import Gtk

class BtngPass(Gtk.Button):

    def __init__(self, lbl, path, parent):
        Gtk.Button.__init__(self, lbl)
        self.path = path
        self.parent = parent
        self.connect("button_press_event", self.btnPGP_clicked)

        #Button Handler for a PGP password file
    def btnPGP_clicked(self, button, x):
        self.parent.clear_status()
        self.parent.clear_account_info()
        self.parent.openAccount = self.get_label()
        self.parent.displayAccount(self.path)
