#18. Graphical User Interfaces
#18.7 Making Your Applications Interactive

# Tkinker's .mainloop() takes care of updating the events_list, and running the event handler anytime a new event is added
#  in the list.
# You just have to define a function for that particular event.

import tkinter as tk

# Create a window object
window= tk.Tk()

# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Run the event loop
window.mainloop()



