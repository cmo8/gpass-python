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
        self.charSets = {}
        self.charLive = []
        self.load_config()

    def add_char_set_stack(self, a, char_sets):
        dic_char_set = {}
        tmp = Gtk.VBox(10)
        #Character Group Title
        title = Gtk.HBox(10)
        tmp.add(title)
        lblCharSetTitle = Gtk.Label("Group Label:")
        title.add(lblCharSetTitle)
        charSetLabel = Gtk.Entry()
        charSetLabel.set_text(a)
        dic_char_set["charLabel"] =  charSetLabel
        title.add(charSetLabel)
        #Character elements
        charSetBox = Gtk.HBox(10)
        tmp.add(charSetBox)
        lblCharSet = Gtk.Label("Character Set:")
        charSetBox.add(lblCharSet)
        charSet = Gtk.Entry()
        charSet.set_text(char_sets)
        dic_char_set["charSet"] =  charSet
        charSetBox.add(charSet)
        #Is Live Check Button
        charSetLiveBox = Gtk.HBox(10)
        checkCharSetLive = Gtk.CheckButton("Character Set is Live")
        set_to_live = False
        if a in self.charLive:
            set_to_live = True
        checkCharSetLive.set_active(set_to_live)
        dic_char_set["charLive"] =  checkCharSetLive
        charSetLiveBox.add(checkCharSetLive)
        btnDelete = Gtk.Button("Delete")
        charSetLiveBox.add(btnDelete)
        btnDelete.connect("clicked", self.btnDelete_clicked)
        tmp.add(charSetLiveBox)
        self.charSets[a] = dic_char_set
        self.stackCharSet.add_titled(tmp, a, a)

    def load_config(self):
        self.folderChooserPasswordStore.set_current_folder(self.config.get_password_store())
        self.fileChooserGPGBinary.set_filename(self.config.get_gpgbinary())
        self.fileChooserGPGHome.set_current_folder(self.config.get_gpghome())
        self.adjustmentPasswordLength.set_value(self.config.get_pass_length())
        char_sets = self.config.get_char_set()
        self.charLive = self.config.get_live_char_set()
        for a in char_sets:
            self.add_char_set_stack(a, char_sets[a])
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

    def btnDelete_clicked(self, button):
        current = self.stackCharSet.get_visible_child_name()
        del self.charSets[current]
        print(self.charSets)
        self.stackCharSet.remove(self.stackCharSet.get_visible_child())
        self.show_all()

    def btnAdd_clicked(self, button):
        self.add_char_set_stack(self.txtCharSetLabel.get_text(), self.txtCharSet.get_text())
        self.show_all()

    def btnSave_clicked(self, button):
        self.config.set_password_store(self.folderChooserPasswordStore.get_current_folder())
        self.config.set_gpgbinary(self.fileChooserGPGBinary.get_filename())
        self.config.set_gpghome(self.fileChooserGPGHome.get_current_folder())
        self.config.set_password_length(int(self.adjustmentPasswordLength.get_value()))
        save_char_sets = {}
        save_live_char_set = []
        for cSet in self.charSets:
            tmp = self.charSets[cSet]
            save_char_sets[tmp["charLabel"].get_text()] = tmp["charSet"].get_text()
            if tmp["charLive"].get_active():
                save_live_char_set.append(cSet)
        self.config.set_char_set(save_char_sets)
        self.config.set_char_live(save_live_char_set)
        self.config.save_config()
        self.parent.passStoreBox.repack_buttons()
        self.parent.setPastView()


    #Show the Window
    def show(self):
        self.show_all()
