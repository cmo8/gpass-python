import sys
from gi.repository import Gio, Gtk
from gPassConfig import GPassConfig
from uiBoxViewManager import BoxViewManager

class GPassApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.cmo.gpass", flags=Gio.ApplicationFlags.FLAGS_NONE)
        #Gtk.Application.new("org.cmo.gpass", 0)
        #reads in the config file
        self.config = GPassConfig()
        self.window = Gtk.ApplicationWindow()


        #self.windowConfigUI = WindowConfigUI(self.config)
        self.connect('activate', self.on_app_activate)
        self.connect('startup', self.on_app_startup)
        self.connect('shutdown', self.on_app_shutdown)

    def on_app_activate(self, app):
        self.window.show_all()

    def on_app_shutdown(self, app):
        # do some cleaning job here, like dumping configuration.
        pass

    def on_app_startup(self, app):
        Gtk.Application.do_startup(self)

        print("start on_app_startup")

        self.menumodel = Gio.Menu()
        self.menumodel.append("Create Password Store", "app.createpasswordstore")
        self.menumodel.append("Open Password Store", "app.openpasswordstore")
        self.menumodel.append("Preferences", "app.preferences")
        self.menumodel.append("About", "app.about")
        self.menumodel.append("Quit", "app.quit")
        self.set_app_menu(self.menumodel)

        cps_action = Gio.SimpleAction.new("createpasswordstore", None)
        cps_action.connect("activate", self.on_action_cps_activated)
        self.add_action(cps_action)

        ops_action = Gio.SimpleAction.new("openpasswordstore", None)
        ops_action.connect("activate", self.on_action_ops_activated)
        self.add_action(ops_action)

        new_action = Gio.SimpleAction.new("preferences", None)
        new_action.connect("activate", self.on_action_preferences_activated)
        self.add_action(new_action)

        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.on_action_about_activated)
        self.add_action(about_action)

        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_action_quit_activated)
        self.add_action(quit_action)

        app.add_window(self.window)

        self.window.set_default_size(850, 400);
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.set_title("GPass")
        self.viewManager = BoxViewManager(self.window, self.config)
        self.window.add(self.viewManager)

        print("on_app_startup Done")

    def on_action_preferences_activated(self, action, user_data):
        self.viewManager.setConfigView()

    def on_action_about_activated(self, action, user_data):
        print('will show about dialog')

    def on_action_quit_activated(self, action, user_data):
        # This will close the default gtk mainloop
        print("Quit gPass")
        self.app.quit()

    def select_repo(self, action):
        #Create a folder
        filechooserdialog = None
        if action == 'select':
            filechooserdialog = Gtk.FileChooserDialog(self.window, title="Open Password Store", buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
            filechooserdialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        elif action == 'create':
            filechooserdialog = Gtk.FileChooserDialog(self.window, title="Create Password Store", buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
            filechooserdialog.set_action(Gtk.FileChooserAction.CREATE_FOLDER)
        email_filter = Gtk.FileFilter()
        email_filter.set_name("Folder")
        email_filter.add_pattern("*")  # whats the pattern for a folder
        filechooserdialog.add_filter(email_filter)
        response = filechooserdialog.run()
        if response == Gtk.ResponseType.OK:
            print("File selected: %s" % filechooserdialog.get_filename())
            #Set config object
            self.config.set_password_store(filechooserdialog.get_filename())
            self.config.config_test()
            self.config.save_config()
            self.viewManager.passStoreBox.repack_buttons()
        filechooserdialog.destroy()

    def on_action_cps_activated(self, action, user_data):
        self.select_repo("create")

    def on_action_ops_activated(self, action, user_data):
        self.select_repo("select")
