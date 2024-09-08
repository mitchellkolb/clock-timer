import random
import gui  # Import the gui module

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
    gui.start_gui(get_random_text)
