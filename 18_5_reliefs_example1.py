#18. Graphical User Interface
#18.5 Working With Widgets
# Example: reliefs
import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE
    }

window = tk.Tk()

for relief_name, relief in border_effects.items():
    # 1
    frame = tk.Frame(master=window, relief = relief, borderwidth=5)

    # 2
    frame.pack(side=tk.LEFT)

    # 3
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

#window.mainloop()

