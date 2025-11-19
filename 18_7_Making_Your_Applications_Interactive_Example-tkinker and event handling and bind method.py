#18. Graphical User Interfaces
#18.7 Making Your Applications Interactive

# Tkinker widgets have a.bind() mtd hthat liks the event to the event handler.
# Let us use the handle_keypress() handler as an example

import tkinter as tk

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()

