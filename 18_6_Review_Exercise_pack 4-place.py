#18. Graphical User Interfaces
#18.6 Review Exercise: Recreate all screenshots in this section
# Exercise 4: .place() geomerty manager:

import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, bg="red", text="I'm at (75,75)")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, bg="yellow", text="I'm at (75,75)")
label2.place(x=75, y=75)

window.mainloop()
