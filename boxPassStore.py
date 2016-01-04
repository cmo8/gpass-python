from gi.repository import Gtk, Gdk
from pypass import PyPass
#from createAccountUI import CreateAccountUI
from popcreateaccount import popCreateAccount
from popdelete import PopDelete
from popadditem import PopAddItem
from popfolder import PopFolder

class BoxPassStore(Gtk.VBox):

    #Constructor
    def __init__(self, config):
        Gtk.VBox.__init__(self, 10)
        #Create PyPass object
        self.gpass_config = config
        self.pypas = PyPass(self.gpass_config)
        self.passDepth = []
        self.openAccount = None
        self.passBtnArray = {}
        self.breadcrumbsBtnArray = {}
        self.accountElements = {}

        #Building UI
        self.builder = Gtk.Builder()
        self.builder.add_from_file("boxPassStore.glade")
        self.builder.connect_signals(self)
        #Application Window
        self.passStorePanel = self.builder.get_object("passStorePanel")
        self.add(self.passStorePanel)
        #Grids
        self.gridData = self.builder.get_object("gridData")
        #Boxes
        self.listbox = self.builder.get_object("boxlist")
        #BUTTONS
        self.checkShow = self.builder.get_object("checkShow")
        self.btnCopyToClipboard = self.builder.get_object("btnCopyToClipboard")
        self.btnNew = self.builder.get_object("btnNew")
        self.btnUpdate = self.builder.get_object("btnUpdate")
        self.btnAddItem = self.builder.get_object("btnAddItem")
        self.btnDelete = self.builder.get_object("btnDelete")
        #Status bar
        self.locationbreadcrumbs = self.builder.get_object("buttonbox")
        self.statusbar = self.builder.get_object("status")
        self.context = self.statusbar.get_context_id("example")
        self.btnDelete.set_sensitive(False)
        self.btnUpdate.set_sensitive(False)
        self.btnAddItem.set_sensitive(False)
        #self.btnMene = self.builder.get_object("btnMene")
        #Text Buffers
        self.txtSearch = self.builder.get_object("txtSearch")
        self.txtPassword = self.builder.get_object("buffertxtPassword")
        self.txtPasswordBox = self.builder.get_object("txtPassword")
        self.txtFile = self.builder.get_object("buffertxtFile")
        #Clipboard
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        #Add pass database buttons
        self.pack_buttons(self.pypas.pass_array())

    #New Button Click Handler
    def btnNew_clicked(self, button):
        self.clear_status()
        self.clear_account_info()
        popcreateaccount = popCreateAccount(self, self.btnNew, self.get_pass_path(), self.pypas)
        popcreateaccount.show()
        #print('btnNew_clicked')

    #Add Item Button Click Handler
    def btnAddItem_clicked(self, button):
        self.clear_status()
        start = self.txtFile.get_start_iter()
        end = self.txtFile.get_end_iter()
        popadditem = PopAddItem(self, self.btnAddItem, self.pypas, self.txtFile.get_text(start, end, True))
        popadditem.show()
        #print("btnAddItem_clicked")

    #Copy the Password to the Clipboard Button Click Handler
    def btnCopyToClipboard_clicked(self, button):
        self.clear_status()
        self.clipboard.set_text(self.txtPassword.get_text(), -1)
        #print('btnCopyToClipboard_clicked')

    #Delete Button Click Handler
    def btnDelete_clicked(self, button):
        self.clear_status()
        popDelete =  PopDelete(self, self.btnDelete, self.pypas)
        popDelete.show()
        #print('btnDelete_clicked')

    #Update Button Click Handler
    def btnUpdate_clicked(self, button):
        self.clear_status()
        start = self.txtFile.get_start_iter()
        end = self.txtFile.get_end_iter()
        self.pypas.insert(self.get_pass_path(), self.txtFile.get_text(start, end, True))
        self.clear_account_info(False)
        self.displayAccount(self.get_pass_path())
        #print('btnUpdate_clicked')

    #Button Handler for a PGP password file
    def btnPGP_clicked(self, button):
        self.clear_status()
        self.clear_account_info()
        self.openAccount = button.get_label()
        self.displayAccount(self.get_pass_path())

    #Move into a selected folder
    def btnFolder_clicked(self, button, event):
        self.clear_status()
        if event.button == 1:
            self.passDepth.append(button.get_label())
            self.repack_buttons()
        elif event.button == 3:
            foldermenu = PopFolder(self, self.listbox, self.pypas)
            foldermenu.show()

    #Update Button Click Handler
    def btnBack_clicked(self, button):
        self.clear_status()
        self.passDepth.pop()
        self.repack_buttons()
        self.clear_account_info()
    #
    def btnMenu_clicked(self, button):
        self.clear_status()
        print("btnMenu_clicked")

    #Handler for the search entity
    def txtSearch_search_changed(self, txt):
        self.new_status("Search: " + self.txtSearch.get_text())
        tmp = self.pypas.find(self.txtSearch.get_text())

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

    #Clear the data from the grid view, txtPassword, and the txtFile
    def clear_account_info(self, clearOpenAccount = True):
        if self.openAccount != None and clearOpenAccount:
            self.openAccount = None
        position = 1
        for element in self.accountElements:
            self.gridData.remove_row(position)
        self.accountElements = {}
        self.txtFile.set_text("", 0)
        self.txtPassword.set_text("", 0)
        self.checkShow.set_active(False)
        self.clipboard.clear()
        self.btnDelete.set_sensitive(False)
        self.btnUpdate.set_sensitive(False)
        self.btnAddItem.set_sensitive(False)
        self.checkShow.set_sensitive(False)
        self.btnCopyToClipboard.set_sensitive(False)

    #Show and hide password
    def checkShow_toggled(self, check):
        active = self.checkShow.get_active()
        self.txtPasswordBox.set_visibility(active)

    #bring window to the top
    def bringToTop(self):
        self.present()

    def get_window(self):
        return self.awindow

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
            if x.endswith('/'):
                self.passBtnArray[x].set_relief(Gtk.ReliefStyle.NONE)
                self.passBtnArray[x].connect("button_press_event", self.btnFolder_clicked)
                #print("Folder: ", pass_tree[x])
            else:
                self.passBtnArray[x].connect("clicked", self.btnPGP_clicked)
                #print("File:   ", pass_tree[x])
            self.listbox.pack_start(self.passBtnArray[x], False, True, 0)
            self.passBtnArray[x].show()
        self.breadcrumbs()

    #Breadcrumbs Button Click
    def breadcrumbs_clicked(self, button):
        target_folder = button.get_label()
        tmp = []
        if not target_folder == "Root":
            target_found = False
            for x in self.passDepth:
                if not target_found:
                    tmp.append(x)
                    if x == target_folder:
                        target_found = True
        self.passDepth = tmp
        self.repack_buttons()

    #Create Breadcrumbs
    def breadcrumbs(self):
        for x in self.breadcrumbsBtnArray:
            self.locationbreadcrumbs.remove(self.breadcrumbsBtnArray[x])
        self.breadcrumbsBtnArray = {}
        if len(self.passDepth) > 0:
            self.breadcrumbsBtnArray["root"] = Gtk.Button("Root")
            self.breadcrumbsBtnArray["root"].set_relief(Gtk.ReliefStyle.NONE)
            self.breadcrumbsBtnArray["root"].connect("clicked", self.breadcrumbs_clicked)
            self.locationbreadcrumbs.add(self.breadcrumbsBtnArray["root"])
            for x in self.passDepth:
                self.breadcrumbsBtnArray[x] = Gtk.Button(x)
                self.breadcrumbsBtnArray[x].set_relief(Gtk.ReliefStyle.NONE)
                self.breadcrumbsBtnArray[x].connect("clicked", self.breadcrumbs_clicked)
                self.locationbreadcrumbs.add(self.breadcrumbsBtnArray[x])
        self.locationbreadcrumbs.show_all()

    #repack the buttons from the boxlist
    def repack_buttons(self):
        self.clear_account_info()
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
        path = "".join(self.passDepth)
        if self.openAccount != None:
            path += self.openAccount
            path += ".gpg"
        #print(path)
        return path

    #Push Status
    def new_status(self, statusMSG):
        self.clear_status()
        self.statusbar.push(self.context, statusMSG)

    #Clear Status bar
    def clear_status(self):
        self.statusbar.remove_all(self.context)
