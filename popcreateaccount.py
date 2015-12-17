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
            if len(self.path) > 0:
                self.path += "/"
            self.path += self.txtAccount.get_text() + '.gpg'
            self.pypas.insert(self.path, self.txtPassword.get_text() + '\n')
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
        self.txtAccountBox.grab_focus()

    #Constructor
    def __init__(self, parent, btn, path, pypas):
        self.parent = parent
        self.pypas = pypas
        self.path = path
        self.btn = btn
        #Creating a popover
        self.popCreate = Gtk.Popover.new(self.btn)
        #Building UI
        self.builder = Gtk.Builder()
        self.builder.add_from_file("popcreateaccount.glade")
        self.builder.connect_signals(self)
        #BUTTONS
        self.btnCancel = self.builder.get_object("btnCancel")
        self.btnSave = self.builder.get_object("btnSave")
        self.btnGenerate = self.builder.get_object("btnGeneratePassword")
        self.checkShow = self.builder.get_object("checkShow")
        #Text Buffers
        self.txtAccount = self.builder.get_object("bufferAccount")
        self.txtPassword = self.builder.get_object("bufferPassword")
        self.txtConfirm = self.builder.get_object("bufferConfirm")
        self.txtAccountBox = self.builder.get_object("txtAccount")
        self.txtPasswordBox = self.builder.get_object("txtPassword")
        self.txtConfirmBox = self.builder.get_object("txtConfirm")
        #Application Window
        hbox = self.builder.get_object("msgCreate")
        tab_list = [self.txtAccountBox,
                    self.txtPasswordBox,
                    self.txtConfirmBox,
                    self.btnSave,
                    self.btnGenerate,
                    self.checkShow,
                    self.btnCancel]
        #self.popDelete.set_focus_chain()
        hbox.set_focus_chain(tab_list)
        self.popCreate.add(hbox)
