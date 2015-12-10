from gi.repository import Gtk
from pypass import PyPass

class CreateAccountUI:

    #New Button Click Handler
    def btnSave_clicked(self, button):
        if self.txtAccount.get_text() == "":
            print "Error No Account information"
        elif self.txtPassword.get_text() == "":
            print "Error No Password Entered"
        elif self.txtConfirm.get_text() == "":
            print "Error No Confirmation Password"
        elif self.txtPassword.get_text() == self.txtConfirm.get_text():
            path = "/".join(self.passDepth)
            if len(self.passDepth) > 0:
                path += "/"
            path += self.txtAccount.get_text()
            self.pypas.insert(path, self.txtPassword.get_text())
            print "Save Account"
        else:
            print "Error Passwords do not match"

    #Show And Hide Password Button Click Handler
    def btnCancel_clicked(self, button):
        print 'btnCancel_clicked'
        self.awindow.destroy()

    #Show the Window
    def show(self):
        self.awindow.show_all()

    #Constructor
    def __init__(self, passDepth, pypas):
        self.passDepth = passDepth
        self.pypas = pypas
        #Building UI
        self.builder = Gtk.Builder()
        self.builder.add_from_file("createMsg.glade")
        self.builder.connect_signals(self)
        #Application Window
        self.awindow = self.builder.get_object("msgCreate")
        self.awindow.set_position(Gtk.WindowPosition.CENTER)
        #BUTTONS
        #self.btnCancel = self.builder.get_object("btnCancel")
        #self.btnSave = self.builder.get_object("btnSave")
        #Text Buffers
        self.txtAccount = self.builder.get_object("bufferAccount")
        self.txtPassword = self.builder.get_object("bufferPassword")
        self.txtConfirm = self.builder.get_object("bufferConfirm")





		
