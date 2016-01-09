from gi.repository import Gtk

class BoxCreateGPGKey(Gtk.VBox):

    #Constructor
    def __init__(self):
        Gtk.VBox.__init__(self)
        #Key name folder
        self.keyNameGroup = Gtk.Box(10)
        self.add(self.keyNameGroup)
        self.lblKeyName = Gtk.Label("Real Name:")
        self.keyNameGroup.add(self.lblKeyName)
        self.txtKeyName = Gtk.Entry()
        self.keyNameGroup.add(self.txtKeyName)

        #Adding email elements
        self.emailGroup = Gtk.Box(10)
        self.add(self.emailGroup)
        self.lblemail = Gtk.Label("Email:")
        self.emailGroup.add(self.lblemail)
        self.txtEmail = Gtk.Entry()
        self.emailGroup.add(self.txtEmail)

        #Adding Password elements
        self.passwordGroup = Gtk.Box(10)
        self.add(self.passwordGroup)
        self.lblPassword = Gtk.Label("Password:")
        self.passwordGroup.add(self.lblPassword)
        self.txtPassword = Gtk.Entry()
        self.passwordGroup.add(self.txtPassword)

        #Adding Password confermation elements
        self.passwordCGroup = Gtk.Box(10)
        self.add(self.passwordCGroup)
        self.lblPasswordC = Gtk.Label("Password:")
        self.passwordCGroup.add(self.lblPasswordC)
        self.txtPasswordC = Gtk.Entry()
        self.passwordCGroup.add(self.txtPasswordC)
        self.show_all()

    def get_real_name(self):
        return self.txtKeyName.get_text()

    def get_email(self):
        return self.txtEmail.get_text()

    def get_password(self):
        return self.txtPassword.get_text()

    def get_confirmation(self):
        return self.txtPasswordC.get_text()