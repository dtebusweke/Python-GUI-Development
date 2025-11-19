#18. Graphical User Interfaces
#18.6 Review Exercise: Recreate all screenshots in this section
# Exercise 6: .grid() geomerty manager - sticky parameter for orgasizing widgets in a frame

import tkinter as tk

window = tk.Tk()

window.columnconfigure([0,1,2,3], weight=1, minsize=250)
window.rowconfigure(0, weight=1, minsize=100)


label1=tk.Label(master=window, text="1", bg="black", fg="white")
label1.grid(row=0, column=0)

label2=tk.Label(master=window, text="2", bg="black", fg="white")
label2.grid(row=0, column=1, sticky="ew")

label3=tk.Label(master=window, text="3", bg="black", fg="white")
label3.grid(row=0, column=2, sticky="ns")

label4=tk.Label(master=window, text="4", bg="black", fg="white")
label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()
