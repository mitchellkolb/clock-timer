import sys
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyGtkApplication")
        GLib.set_application_name('My Gtk Application')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Hello World")
        
        # Setting the default window size (width x height) cause standard is too small
        window.set_default_size(450, 500)
        
        window.present()

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
