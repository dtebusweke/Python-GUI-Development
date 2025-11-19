#18. Graphical User Interfaces
#18.6 Controlling Layout With Geometry Managers
# By default, widgets are placed in the center of their grid cells.
# With the .grid()'s sticky parameter, you can combinme the letters to position a lable in the grid cell as below

import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, weight=1, minsize=50)
window.columnconfigure([0,1,2,3], weight=1, minsize=50)

#no frame widgets this time, we use lables directly with the .grid method
label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()
