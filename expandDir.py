import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gpassconfig import GPassConfig
from pypass import PyPass

class ExpandDir(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.box = Gtk.VBox(10)
        self.add(self.box)

        self.passConfig = GPassConfig()
        self.pypass = PyPass(self.passConfig)
        listdir = self.pypass.build_gpg_tree(self.passConfig.password_store)
        print(listdir)
        self.password_store_dir = Gtk.Expander()
        self.password_store_dir.set_label("Password Store")
        self.children = Gtk.VBox(10)
        self.password_store_dir.add(self.children)
        self.build_expand(listdir, self.children)
        self.box.pack_start(self.password_store_dir, False, True, 0)

    #Button Handler for a PGP password file
    def btnPGP_clicked(self, button):
        self.clear_account_info()
        self.openAccount = button.get_label()
        self.displayAccount(self.get_pass_path())

    def build_expand(self, listdir, ui):
        for d in listdir:
            print(type(listdir))
            if type(listdir[d]) == type({}):
                print(" - ", d, " => ", listdir[d])
                expander = Gtk.Expander()
                expander.set_label(d)
                box = Gtk.VBox(10)
                expander.add(box)
                ui.add(expander)
                self.build_expand(listdir[d], box)
            else:
                print("+ ", d)
                btn = Gtk.Button(d)
                btn.connect("clicked", self.btnPGP_clicked)
                ui.add(btn)
        #return ui

    #displays the selected account
    def displayAccount(self, accountToDisplay):
        #Get GPG file content
        account_info = self.pypas.account(accountToDisplay)
        #display contents in text editor
        self.txtFile.set_text(str(account_info))
        #Split the lines appert
        account_lines = account_info.split('\n')
        #place password in text box
        self.txtPassword.set_text(account_lines[0], len(account_lines[0]))
        account_lines.remove(account_lines[0])
        top = 1
        for line in account_lines:
            #Split the line into key => value
            row = line.split(': ')
            if len(row) == 2:
                #Create GtkLabel
                lbl = Gtk.Label(row[0].title() + ':')
                lbl.set_justify(Gtk.Justification.RIGHT)
                #Create GtkTextbox
                txt = Gtk.Entry()
                txt.set_text(row[1])
                #Add Label and Textbox to the array
                self.accountElements[row[1]] = txt
                self.gridData.attach(lbl, 0, top, 1, 1)
                self.gridData.attach_next_to(txt, lbl, Gtk.PositionType.RIGHT, 1, 1)
                top += 1
            self.gridData.show_all()
        self.btnDelete.set_sensitive(True)
        self.btnUpdate.set_sensitive(True)
        self.btnAddItem.set_sensitive(True)
        self.checkShow.set_sensitive(True)
        self.btnCopyToClipboard.set_sensitive(True)

win = ExpandDir()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
