import random
from guiFile import RandomTextWindow, start_gui  # Import the correct names from guiFile

# Define a list of random text strings
random_text_list = [
    "Hello, World!",
    "Welcome to PyGObject!",
    "Random Text Here",
    "Enjoy coding in Python!",
    "Linux Mint is awesome!"
]

def get_random_text():
    """Return a random text from the list."""
    return random.choice(random_text_list)

if __name__ == "__main__":
    # Pass the random text function to the GUI and start it
    start_gui(get_random_text)  # Use start_gui from guiFile



# import sys
# import gi

# gi.require_version("Gtk", "4.0")
# from gi.repository import GLib, Gtk

# class MyApplication(Gtk.Application):
#     def __init__(self):
#         super().__init__(application_id="com.example.MyGtkApplication")
#         GLib.set_application_name('My Gtk Application')

#     def do_activate(self):
#         window = Gtk.ApplicationWindow(application=self, title="Hello World")
        
#         # Setting the default window size (width x height) cause standard is too small
#         window.set_default_size(450, 500)
        
#         window.present()

# app = MyApplication()
# exit_status = app.run(sys.argv)
# sys.exit(exit_status)