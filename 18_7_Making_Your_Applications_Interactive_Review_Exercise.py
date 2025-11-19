#18. Graphical User Interfaces
#18.7 Making Your Applications Interactive

# Review Exercise

#1. Write a program that displays a single button with the default background color and black text that reads "Click me".


import tkinter as tk
import random

list_colors = ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]

def click():
    color = random.choice(list_colors)
    button["bg"] = color
    
window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

button = tk.Button(master=window, text="Click me", command=click)
button.grid(row=0, column=0, sticky="nsew")

window.mainloop()


#2. Write a program that simulates rolling a six-sided die. There should be one button with the text "Roll".
#   When the user clicks the button, a random integer from 1 to 6 should be displayed.

window = tk.Tk()

def die_roll():
    label["text"] = str(random.randint(1,6))

window.columnconfigure(0, minsize=150, weight=1)
window.rowconfigure([0,1], minsize=50, weight=1)

button = tk.Button(master=window, text="Roll", command=die_roll)
button.grid(row=0, column=0, sticky="nsew")

label = tk.Label(master=window, text="")
label.grid(row=1, column=0, sticky="nsew")

window.mainloop()
