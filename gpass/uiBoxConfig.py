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
        self.fileChooserGPGBinary = self.builder.get_object("fileChooserGPGBinary")
        self.fileChooserGPGHome = self.builder.get_object("fileChooserGPGHome")
        self.adjustmentPasswordLength = self.builder.get_object("adjustmentPasswordLength")
        self.stackSidebarCharSets = self.builder.get_object("stackSidebarCharSets")
        self.stackCharSet = self.builder.get_object("stackCharSet")
        self.txtCharSetLabel = self.builder.get_object("txtCharSetLabel")
        self.txtCharSet = self.builder.get_object("txtCharSet")
        self.load_config()

    def load_config(self):
        self.folderChooserPasswordStore.set_current_folder(self.config.get_password_store())
        self.fileChooserGPGBinary.set_filename(self.config.get_gpgbinary())
        self.fileChooserGPGHome.set_current_folder(self.config.get_gpghome())
        self.adjustmentPasswordLength.set_value(self.config.get_pass_length())
        char_sets = self.config.get_char_set()
        live_char_set = self.config.get_live_char_set()
        for a in char_sets:
            tmp = Gtk.VBox(10)
            #Character Group Title
            title = Gtk.HBox(10)
            tmp.add(title)
            lblCharSetTitle = Gtk.Label("Group Label:")
            title.add(lblCharSetTitle)
            charSetLabel = Gtk.Entry()
            charSetLabel.set_text(a)
            title.add(charSetLabel)
            #Character elements
            charSetBox = Gtk.HBox(10)
            tmp.add(charSetBox)
            lblCharSet = Gtk.Label("Character Set:")
            charSetBox.add(lblCharSet)
            charSet = Gtk.Entry()
            charSet.set_text(char_sets[a])
            charSetBox.add(charSetLabel)
            #Is Live Check Button
            checkCharSetLive = Gtk.CheckButton("Character Set is Live:")
            set_to_live = False
            if a in live_char_set:
                set_to_live = True
            checkCharSetLive.set_active(set_to_live)
            tmp.add(checkCharSetLive)
            self.stackCharSet.add_named(tmp, a)
        self.show_all()
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
