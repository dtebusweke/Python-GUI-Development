#18. Graphical User Interfaces
#18.6 Controlling Layout With Geometry Managers

# Creating frames and putting them in a window with .grid() geometry manager, make sure the grid rows and columns are responsive to window resizing.

import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    
    for j in range(3):
        frame=tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=1, pady=1)

        label=tk.Label(master = frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=1, pady=1)


window.mainloop()
        
