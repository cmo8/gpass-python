import random
import string
from gi.repository import Gtk
#from gpasss import PyPass

class popCreateAccount:

    #Constructor
    def __init__(self, parent, btn, path):
        self.parent = parent
        self.gpass = self.parent.gpass
        self.path = path
        self.btn = btn
        #Text Buffers
        self.txtAccount = Gtk.Entry()
        self.txtPassword = Gtk.Entry()
        self.txtConfirm = Gtk.Entry()
        self.btnSave = Gtk.Button("Save")
        self.btnCheckShow = Gtk.CheckButton("Show")
        #Creating a popover
        self.popCreate = self.create_account_popover_menu()

    #Create the Delete poperover confirm menu
    def create_account_popover_menu(self):
        popover = Gtk.Popover.new(self.btn)
        gbox = Gtk.Grid()
        gbox.set_column_spacing(10)
        gbox.set_row_spacing(10)
        popover.add(gbox)

        labelAccount = Gtk.Label("Account: ")
        gbox.attach(labelAccount,    0, 0, 1, 1)
        gbox.attach(self.txtAccount, 1, 0, 1, 1)

        labelPass = Gtk.Label("Password: ")
        btnGenerate = Gtk.Button("Generate")
        btnGenerate.connect("clicked", self.btnGeneratePassword_clicked)
        gbox.attach(labelPass,        0, 1, 1, 1)
        gbox.attach(self.txtPassword, 1, 1, 1, 1)
        gbox.attach(btnGenerate,      2, 1, 1, 1)

        labelPassConf = Gtk.Label("Password: ")
        self.btnCheckShow.connect("clicked", self.checkShow_toggled)
        gbox.attach(labelPassConf,     0, 2, 1, 1)
        gbox.attach(self.txtConfirm,   1, 2, 1, 1)
        gbox.attach(self.btnCheckShow, 2, 2, 1, 1)

        active = self.btnCheckShow.get_active()
        self.txtPassword.set_visibility(active)
        self.txtConfirm.set_visibility(active)

        btnCancel = Gtk.Button("Cancel")
        btnCancel.connect("clicked", self.btnCancel_clicked)
        self.btnSave.connect("clicked", self.btnSave_clicked)
        gbox.attach(btnCancel,    1, 3, 1, 1)
        gbox.attach(self.btnSave, 2, 3, 1, 1)

        return popover

    #New Button Click Handler
    def btnSave_clicked(self, button):
        if self.txtAccount.get_text() == "":
            #self.txtAccountBox.
            self.parent.new_status("Error No Account information")
            #print("Error No Account information")
        elif self.txtPassword.get_text() == "":
            self.parent.new_status("Error No Password Entered")
            #print("Error No Password Entered")
        elif self.txtConfirm.get_text() == "":
            self.parent.new_status("Error No Confirmation Password")
            #print("Error No Confirmation Password")
        elif self.txtPassword.get_text() == self.txtConfirm.get_text():
            if len(self.path) == 0:
                self.path += "/"
            self.path += self.txtAccount.get_text() + '.gpg'
            self.gpass.insert(self.path, self.txtPassword.get_text() + '\n')
            self.parent.new_status("Saved Account:" + self.txtAccount.get_text())
            #print("Save Account")
            self.parent.repack_buttons()
            self.popCreate.hide()
        else:
            self.parent.new_status("Error Passwords do not match")
            #print("Error Passwords do not match")

    #Show And Hide Password Button Click Handler
    def btnCancel_clicked(self, button):
        self.popCreate.hide()
        #print('btnCancel_clicked')

    #Show And Hide Password Button Click Handler
    def btnGeneratePassword_clicked(self, button):
        gen = "R@nd0m"
        char_set = self.parent.config.get_active_char_group()
        gen = ''.join(random.sample(char_set*6, self.parent.config.get_pass_length()))
        self.txtPassword.set_text(gen)
        self.txtConfirm.set_text(gen)
        #print('btnGeneratePassword_clicked')
        self.btnSave.grab_focus()

    #Show and hide the
    def checkShow_toggled(self, check):
        active = self.btnCheckShow.get_active()
        self.txtPassword.set_visibility(active)
        self.txtConfirm.set_visibility(active)

    #Show the Menu
    def show(self):
        self.popCreate.show_all()
        self.txtAccount.grab_focus()


