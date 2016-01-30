from gi.repository import Gtk, Gdk
from gPassGPG import GPassGPG
from uiBoxCreateGPGKey import BoxCreateGPGKey

class BoxConfig(Gtk.VBox):

    #Constructor
    def __init__(self, parent):
        Gtk.VBox.__init__(self, 10)
        self.parent = parent
        self.config = self.parent.config
        self.gpg = GPassGPG(self.config.gpgbinary, self.config.gpghome)
        #self.set_default_size(700, 350);
        #self.set_position(Gtk.WindowPosition.CENTER)
        #self.set_title("GPass Settings")

        #Building UI

        self.builder = Gtk.Builder()
        self.builder.add_from_file("gpass/uiBoxConfig.glade")
        self.builder.connect_signals(self)
        #Application Window
        self.passBoxConfig = self.builder.get_object("boxconfig")

        self.add(self.passBoxConfig)
        self.boxGenGPGKey = self.builder.get_object("boxGenGPGKey")
        self.boxCreateGPGKey = BoxCreateGPGKey()
        self.boxGenGPGKey.add(self.boxCreateGPGKey)
        self.btnGenKey = Gtk.Button('Generate GPG Key')
        self.btnGenKey.connect("clicked", self.btnCreateGPGKey_clicked)
        self.boxGenGPGKey.pack_end(self.btnGenKey, True, True, 0)

        #folderChooserPasswordStore
        self.folderChooserPasswordStore = self.builder.get_object("folderChooserPasswordStore")
        #fileChooserGPGBinary
        self.fileChooserGPGBinary = self.builder.get_object("fileChooserGPGBinary")
        #fileChooserGPGHome
        self.fileChooserGPGHome = self.builder.get_object("fileChooserGPGHome")
        #scalePasswordLength
        self.adjustmentPasswordLength = self.builder.get_object("adjustmentPasswordLength")
        #stackSidebarCharSets
        self.stackSidebarCharSets = self.builder.get_object("stackSidebarCharSets")
        #txtCharSetLabel
        self.txtCharSetLabel = self.builder.get_object("txtCharSetLabel")
        #txtCharSet
        self.txtCharSet = self.builder.get_object("txtCharSet")
        self.load_config()

    def load_config(self):
        self.adjustmentPasswordLength.set_value(self.config.get_pass_length())
        pass

    def btnCreateGPGKey_clicked(self, button):
        real_name = boxCreateGPGKey.get_real_name()
        email = boxCreateGPGKey.get_email()
        password = boxCreateGPGKey.get_password()
        passwordc = boxCreateGPGKey.get_confirmation()
        if real_name != "" and email != "" and password != "" and passwordc != "" and password == passwordc:
            print("Real Name:", real_name)
            print("Email:", email)
            self.gpg.generate_key(real_name, email, password)

    def btnCancel_clicked(self, button):
        self.parent.setPastView()

    def btnAdd_clicked(self, button):
        print('btnAdd_clicked')

    def btnSave_clicked(self, button):
        print('btnSave_clicked')

    #Show the Window
    def show(self):
        self.show_all()
