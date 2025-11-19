#18. Graphical User Interfaces
#18.7 Making Your Applications Interactive

# handle_keypress() function to handle keypress events.

events_list = []

# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

while True:
    if events_list == []:
        continue
    
    event = events_list[0]

    # If event is a keypress event object
    if event.type == "keypress":
        # Call the keypress event handler
        handle_keypress(event)

