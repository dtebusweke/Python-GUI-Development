#18. Graphical User Interfaces
#18.6 Controlling Layouts With Geometry Managers

import tkinter as tk

window = tk.Tk()

#1
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

#2
label1 = tk.Label(master=frame, text="I'm at (0,0)", bg="red")
label1.place(x=0, y=0)

#3
label2 = tk.Label(master=frame, text="I'm at (75,75)", bg="yellow")
label2.place(x=75, y=75)

window.mainloop()
