from gi.repository import Gtk
from pypass import PyPass

class CreateMsgUI:

    #New Button Click Handler
    def btnSave_clicked(self, button):
        if txtAccount.get_text() == "":
            print "Error No Account information"
        elif txtPassword.get_text() == "":
            print "Error No Password Entered"
        elif txtConfirm.get_text() == "":
            print "Error No Confirmation Password"
        elif txtPassword.get_text() == txtConfirm.get_text()
            self.pypas.insert(txtAccount.get_text(), txtPassword.get_text())
            print "Save Account"
        else
            print "Error Passwords do not match"

    #Show And Hide Password Button Click Handler
    def btnCancel_clicked(self, button):
        print 'btnCancel_clicked'

    #Show the Window
    def show(self):
        self.awindow.show_all()

    #Constructor
    def __init__(self, path):
        self.path = path
        #Building UI
        self.builder = Gtk.Builder()
        self.builder.add_from_file("createMsg.glade")
        self.builder.connect_signals(self)
        #Application Window
        self.awindow = self.builder.get_object("msgCreate")
        self.awindow.set_position(Gtk.WindowPosition.CENTER)
        #BUTTONS
        self.btnCancel = self.builder.get_object("btnCancel")
        self.btnSave = self.builder.get_object("btnSave")
        #Text Buffers
        self.txtAccount = self.builder.get_object("bufferAccount")
        self.txtPassword = self.builder.get_object("bufferPassword")
        self.txtConfirm = self.builder.get_object("bufferConfirm")





		
