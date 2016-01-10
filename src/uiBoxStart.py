import os
from git import Repo
from gi.repository import Gtk
from gPassGPG import GPassGPG
from uiDialogCreatePassStore import DialogCreatePassStore
from uiDialogClonePassStoreRepo import DialogClonePassStoreRepo

class BoxStart(Gtk.VButtonBox):

    def __init__(self, parent):
        Gtk.VButtonBox.__init__(self)
        self.parent = parent
        self.config = self.parent.config
        self.gpg = GPassGPG(self.config.gpgbinary, self.config.gpghome)

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
        print('btnCreatePassStore_clicked')
        keys = self.gpg.list_keys(True)
        self.gpg.list_public_keys()
        dialogCreatePassStore = DialogCreatePassStore(self.parent, keys)
        print('btnCreatePassStore_clicked')
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
                self.parent.gpass.create(real_name, dialogCreatePassStore.txtLocation.get_text())
                self.config.save_config()
                self.parent.setPassStoreView()
                print("OK button clicked")
            elif response == Gtk.ResponseType.CANCEL:
                loop_continue = True
                print("Cancel button clicked")
            else:
                loop_continue = True
                print("Dialog closed")
        dialogCreatePassStore.destroy()

    def btnSelectPassStore_clicked(self, button):
        #Create a folder
        filechooserdialog = Gtk.FileChooserDialog(self.parent, title="Open Password Store", buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        filechooserdialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        email_filter = Gtk.FileFilter()
        email_filter.set_name("Folder")
        email_filter.add_pattern("*")  # whats the pattern for a folder
        filechooserdialog.add_filter(email_filter)
        response = filechooserdialog.run()
        if response == Gtk.ResponseType.OK:
            directory = filechooserdialog.get_filename()
            print("File selected: %s" % directory)
            #Set config object
            self.config.set_password_store(directory)
            self.config.save_config()
            self.parent.setPassStoreView()
        filechooserdialog.destroy()
        print('btnSelectPassStore_clicked')

    def btnGitClonePassStore_clicked(self, button):
        dialogClonePassStoreRepo = DialogClonePassStoreRepo(self.parent)
        response = dialogClonePassStoreRepo.run()

        if response == Gtk.ResponseType.OK:
            repo_dir = dialogClonePassStoreRepo.txtLocation.get_text()
            git_url = dialogClonePassStoreRepo.txtRepo.get_text()
            print("Location:", repo_dir)
            print("Repo:", git_url)
            print("OK button clicked")
            Repo.clone_from(git_url, repo_dir)
            self.config.set_password_store(repo_dir)
            self.config.save_config()
            self.parent.setPassStoreView()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel button clicked")
        else:
            print("Dialog closed")
        dialogClonePassStoreRepo.destroy()