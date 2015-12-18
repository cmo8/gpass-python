from gi.repository import Gtk
import random
from pypass import PyPass

class CreateAccountUI:

    #Constructor
    def __init__(self, parent, passDepth, pypas):
        self.parent = parent
        self.passDepth = passDepth
        self.pypas = pypas
        #Building UI
        self.builder = Gtk.Builder()
        self.builder.add_from_file("createAccountUI.glade")
        self.builder.connect_signals(self)
        #Application Window
        self.awindow = self.builder.get_object("msgCreate")
        self.awindow.set_transient_for(parent.get_window())
        self.awindow.set_position(Gtk.WindowPosition.CENTER)
        #BUTTONS
        self.btnCancel = self.builder.get_object("btnCancel")
        self.btnSave = self.builder.get_object("btnSave")
        self.checkShow = self.builder.get_object("checkShow")
        #Text Buffers
        self.txtAccount = self.builder.get_object("bufferAccount")
        self.txtPassword = self.builder.get_object("bufferPassword")
        self.txtConfirm = self.builder.get_object("bufferConfirm")
        self.txtPasswordBox = self.builder.get_object("txtPassword")
        self.txtConfirmBox = self.builder.get_object("txtConfirm")

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
            self.parent.repack_buttons()
            self.awindow.destroy()
        else:
            print "Error Passwords do not match"

    #Show And Hide Password Button Click Handler
    def btnCancel_clicked(self, button):
        print 'btnCancel_clicked'
        self.awindow.destroy()

    #Show And Hide Password Button Click Handler
    def btnGeneratePassword_clicked(self, button):
        gen = "R@nd0m"
        self.txtPassword.set_text(gen, len(gen))
        self.txtConfirm.set_text(gen, len(gen))
        print 'btnGeneratePassword_clicked'
        self.btnSave.grab_focus()

    #Show and hide the
    def checkShow_toggled(self, check):
        active = self.checkShow.get_active()
        self.txtPasswordBox.set_visibility(active)
        self.txtConfirmBox.set_visibility(active)

    #Show the Window
    def show(self):
        self.awindow.show_all()

