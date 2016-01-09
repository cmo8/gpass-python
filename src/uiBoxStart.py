import os
from gi.repository import Gtk
from gpgkey import GPGkey
from dialogCreatePassStore import DialogCreatePassStore

from dialogClonePassStoreRepo import DialogClonePassStoreRepo

class BoxStart(Gtk.VButtonBox):

    def __init__(self, parent, config):
        Gtk.VButtonBox.__init__(self)
        self.parent = parent
        self.config = config
        self.gpg = GPGkey(self.config.gpgbinary, self.config.gpghome)

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
        keys = self.gpg.list_keys()
        self.gpg.list_public_keys()
        dialogCreatePassStore = DialogCreatePassStore(self.parent, self.config, keys)
        
        loop_continue = False
        while not loop_continue:
            response = dialogCreatePassStore.run()
            if response == Gtk.ResponseType.OK:
                real_name = ''
                if dialogCreatePassStore.gen_key:
                    real_name = dialogCreatePassStore.createGPGkey.get_real_name()
                    email = dialogCreatePassStore.createGPGkey.get_email()
                    password = dialogCreatePassStore.createGPGkey.get_password()
                    passwordc = dialogCreatePassStore.createGPGkey.get_confirmation()
                    if real_name != "" and email != "" and password != "" and passwordc != "" and password == passwordc:
                        print("Real Name:", real_name)
                        print("Email:", email)
                        self.gpg.generate_key(real_name, email, password)
                        #self.config.set_gpgkey(email)
                        loop_continue = True
                    else:
                        print("Can NOT Generate Key!!")
                        pass
                else:
                    real_name = dialogCreatePassStore.selected_key
                    loop_continue = True
                self.parent.pypas.create(real_name, dialogCreatePassStore.txtLocation.get_text())
                print("OK button clicked")
            elif response == Gtk.ResponseType.CANCEL:
                loop_continue = True
                print("Cancel button clicked")
            else:
                loop_continue = True
                print("Dialog closed")
        dialogCreatePassStore.destroy()
        self.config.save_config()
        self.parent.setPassStoreView()
        print('btnCreatePassStore_clicked')

    def btnSelectPassStore_clicked(self, button):
        print('btnSelectPassStore_clicked')

    def btnGitClonePassStore_clicked(self, button):
        dialogClonePassStoreRepo = DialogClonePassStoreRepo(self.parent, self.config)
        response = dialogClonePassStoreRepo.run()

        if response == Gtk.ResponseType.OK:
            location = dialogClonePassStoreRepo.txtLocation.get_text()
            repo = dialogClonePassStoreRepo.txtRepo.get_text()
            print("Location:", location)
            print("Repo:", repo)
            print("OK button clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")
        else:
            print("Dialog closed")
        dialogClonePassStoreRepo.destroy()