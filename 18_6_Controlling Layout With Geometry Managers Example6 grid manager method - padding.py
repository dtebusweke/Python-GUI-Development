#18. Graphical User Interfaces
#18.6 Controlling Layout With Geometry Managers
# Example about padding application on both .pack() and .grid gemetry managers

import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief = tk.RAISED,
            borderwidth = 1
            )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text = f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()
