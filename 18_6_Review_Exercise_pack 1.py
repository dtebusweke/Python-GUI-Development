#18. Graphical User Interfaces
#18.6 Review Exercise: Recreate all screenshots in this section
# Exercise 1: .pack() places each frame below the previous one in the order they're assigned to the window:

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()

window.mainloop()
