import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class RandomTextWindow(Gtk.Window):
    def __init__(self, get_random_text_func):
        super().__init__(title="Random Text Window")
        
        # Set the window size to be a vertical rectangle
        self.set_default_size(200, 400)
        
        # Create a label to display the random text
        self.label = Gtk.Label(label="")
        self.label.set_line_wrap(True)  # Enable text wrapping
        self.label.set_justify(Gtk.Justification.CENTER)  # Center the text

        # Get random text from the passed function
        random_text = get_random_text_func()
        self.label.set_text(random_text)

        # Add the label to the window
        self.add(self.label)

def start_gui(get_random_text_func):
    """Initialize the GTK application and open the window."""
    win = RandomTextWindow(get_random_text_func)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
