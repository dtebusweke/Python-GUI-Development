#18. Graphical User Interfaces
#18.6 Controlling Layout With Geometry Managers
# By default, widgets are placed in the center of their grid cells as illustrated by below example of a one clumn and two rows grid

import tkinter as tk

window = tk.Tk()

window.columnconfigure(0, weight=1, minsize=250)
window.rowconfigure([0,1], weight=1, minsize=100)

#no frame widgets this time, we use lables directly with the .grid method
label1 = tk.Label(master=window, text="A")
label1.grid(row=0, column=0)

label2 = tk.Label(master=window, text="B")
label2.grid(row=1, column=0)

window.mainloop()
