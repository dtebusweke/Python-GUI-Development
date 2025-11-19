#18. Graphical User Interfaces
#18.6 Controlling Layout With Geometry Managers
#Example: .pack() grid manager

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window, height=25, width=25, bg="blue")
frame3.pack()

window.mainloop()
