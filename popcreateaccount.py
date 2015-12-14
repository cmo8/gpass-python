from gi.repository import Gtk
from pypass import PyPass

class popCreateAccount:
    #Create the Delete poperover confirm menu
    def create_account_popover_menu(self):

        return popover

    #New Button Click Handler
    def btnSave_clicked(self, button):
        if self.txtAccount.get_text() == "":
            #self.txtAccountBox.
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
            self.popCreate.hide()
        else:
            print "Error Passwords do not match"

    #Show And Hide Password Button Click Handler
    def btnCancel_clicked(self, button):
        self.popCreate.hide()
        print 'btnCancel_clicked'

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

    #Show the Menu
    def show(self):
        self.popCreate.show_all()

    #Constructor
    def __init__(self, btn, passDepth, pypas):
        self.pypas = pypas
        self.passDepth = passDepth
        self.btn = btn
        #Creating a popover
        self.popCreate = Gtk.Popover.new(self.btn)
        #Building UI
        self.builder = Gtk.Builder()
        self.builder.add_from_file("popcreateaccount.glade")
        self.builder.connect_signals(self)
        #Text Buffers
        self.txtAccount = self.builder.get_object("bufferAccount")
        self.txtPassword = self.builder.get_object("bufferPassword")
        self.txtConfirm = self.builder.get_object("bufferConfirm")
        self.txtAccountBox = self.builder.get_object("txtAccount")
        self.txtPasswordBox = self.builder.get_object("txtPassword")
        self.txtConfirmBox = self.builder.get_object("txtConfirm")
        #Application Window
        hbox = self.builder.get_object("msgCreate")
        self.popCreate.add(hbox)