from gi.repository import Gtk
from dialogCreatePassStore import DialogCreatePassStore

from dialogClonePassStoreRepo import DialogClonePassStoreRepo

class BoxStart(Gtk.VButtonBox):

    def __init__(self,parent, config):
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
        dialogCreatePassStore = DialogCreatePassStore(self.parent, self.config, keys)
        loop_continue = false
        while not loop_continue:
            response = dialogCreatePassStore.run()
            if response == Gtk.ResponseType.OK:
                if dialogCreatePassStore.gen_key:
                    real_name = dialogCreatePassStore.txtKeyName.get_text()
                    email = dialogCreatePassStore.txtEmail.get_text()
                    password = dialogCreatePassStore.txtPassword.get_text()
                    passwordc = dialogCreatePassStore.txtPasswordC.get_text()
                    if real_name != "" and email != "" and password != "" and passwordc != "" and password == passwordc:
                        print("Real Name:", real_name)
                        print("Email:", email)
                        self.gpg.generate_key(real_name, email, password)
                        self.config.set_gpgkey(email)
                        loop_continue = True
                    else:
                        print("Can NOT Generate Key!!")
                else:
                    key_id = dialogCreatePassStore.selected_key
                    self.config.set_gpgkey(key_id)
                self.config.set_password_store(dialogCreatePassStore.txtLocation.get_text())
                print("Password Store Home:", )
                os.mkdir(self.config.get_password_store)
                loop_continue = True
                print("OK button clicked")
            elif response == Gtk.ResponseType.CANCEL:
                loop_continue = True
                print("Cancel button clicked")
            else:
                loop_continue = True
                print("Dialog closed")
            pass

        dialogCreatePassStore.destroy()
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