from gi.repository import Gtk
from pypass import PyPass
from createMsg import CreateMsgUI

class PassUI:

    #New Button Click Handler
    def btnNew_clicked(self, button):
        createMsg = CreateMsgUI(self.passDepth, self.pypas)
        createMsg.show()
        print 'btnNew_clicked'

    #Show And Hide Password Button Click Handler
    def btnShowPassword_clicked(self, button):
        print 'btnShowPassword_clicked'

    #Copy the Password to the Clipboard Button Click Handler
    def btnCopyToClipboard_clicked(self, button):
        print 'btnCopyToClipboard_clicked'

    #Delete Button Click Handler
    def btnDelete_clicked(self, button):
        print 'btnDelete_clicked'

    #Update Button Click Handler
    def btnUpdate_clicked(self, button):
        print 'btnUpdate_clicked'

    #Button Handler for a PGP password file
    def btnPGP_clicked(self, button):
        act = self.get_pass_path()
        if len(act) > 0:
            act += "/"
        act += button.get_label()
        txt = self.pypas.account(act)
        self.txtFile.set_text(str(txt))

    def btnFolder_clicked(self, button):
        self.passDepth.append(button.get_label())
        self.repack_buttons()

    #Update Button Click Handler
    def btnBack_clicked(self, button):
        self.passDepth.pop()
        self.repack_buttons()
    #
    def btnMenu_clicked(self, button):
        print "btnMenu_clicked"

    #Show the Window
    def show(self):
        self.awindow.show_all()

    #Pack the buttons into the boxlist
    def pack_buttons(self, pass_tree):
        if len(self.passDepth) > 0:
            back = "back"
            self.passBtnArray[back] = Gtk.Button("Back")
            self.passBtnArray[back].connect("clicked", self.btnBack_clicked)
            self.listbox.pack_start(self.passBtnArray[back], False, True, 0)
            self.passBtnArray[back].show()
        for x in pass_tree:
            self.passBtnArray[x] = Gtk.Button(x)
            if type(pass_tree[x])==type({}):
                self.passBtnArray[x].set_relief(Gtk.ReliefStyle.NONE)
                self.passBtnArray[x].connect("clicked", self.btnFolder_clicked)
                #print "Folder: ", pass_tree[x]
            else:
                self.passBtnArray[x].connect("clicked", self.btnPGP_clicked)
                #print "File:   ", pass_tree[x]
            self.listbox.pack_start(self.passBtnArray[x], False, True, 0)
            self.passBtnArray[x].show()

    #repack the buttons from the boxlist
    def repack_buttons(self):
        for x in self.passBtnArray:
            self.listbox.remove(self.passBtnArray[x])
        self.passBtnArray = {}
        if len(self.passDepth) > 0:
            path = self.get_pass_path()
            self.pack_buttons(self.pypas.pass_array(path))
        else:
            self.pack_buttons(self.pypas.pass_array())

    #get the current path
    def get_pass_path(self):
        return "/".join(self.passDepth)

    #Constructor
    def __init__(self):
        #Create PyPass object
        self.pypas = PyPass()
        self.passDepth = []
        self.passBtnArray = {}
        #Building UI
        self.builder = Gtk.Builder()
        self.builder.add_from_file("passui.glade")
        self.builder.connect_signals(self)
        #Application Window
        self.awindow = self.builder.get_object("applicationwindow1")
        self.awindow.set_default_size (700, 300);
        self.awindow.set_position(Gtk.WindowPosition.CENTER)
        self.awindow.connect("destroy", Gtk.main_quit)
        #Grids
        self.gridData = self.builder.get_object("gridData")
        #Boxes
        self.listbox = self.builder.get_object("boxlist")
        #BUTTONS
        self.btnShowPassword = self.builder.get_object("btnShowPassword")
        self.btnCopyToClipboard = self.builder.get_object("btnCopyToClipboard")
        self.btnNew = self.builder.get_object("btnNew")
        self.btnUpdate = self.builder.get_object("btnUpdate")
        self.btnDelete = self.builder.get_object("btnDelete")
        self.btnMene = self.builder.get_object("btnMene")
        #Text Buffers
        self.txtPassword = self.builder.get_object("buffertxtPassword")
        self.txtFile = self.builder.get_object("buffertxtFile")
        #Add pass database buttons
        self.pack_buttons(self.pypas.pass_array())





		
