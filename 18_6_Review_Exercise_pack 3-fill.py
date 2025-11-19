#18. Graphical User Interfaces
#18.6 Review Exercise: Recreate all screenshots in this section
# Exercise 3: .pack() has a side keyword that specifies where each frame should be placed. Options are:
# tk.TOP
# tk.BOTTOM
# tk.LEFT
# tk.RIGHT

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(side = tk.LEFT, fill = tk.BOTH, expand=True)

frame2 = tk.Frame(master=window, width=50, bg="yellow")
frame2.pack(side = tk.LEFT, fill =  tk.BOTH, expand=True)

frame3 = tk.Frame(master=window, width=25, bg="blue")
frame3.pack(side = tk.LEFT, fill = tk.BOTH, expand=True)

window.mainloop()
