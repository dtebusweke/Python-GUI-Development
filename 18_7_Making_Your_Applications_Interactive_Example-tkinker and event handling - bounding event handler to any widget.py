#18. Graphical User Interfaces
#18.7 Making Your Applications Interactive

# You can bind an event handler to any widget in your application
# Example below shows binding an event handler to a Button widget that will perform some action
#  whenever the button is pressed.

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>" , handle_click)
