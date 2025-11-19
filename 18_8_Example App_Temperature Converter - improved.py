#18. Graphical User Interfaces
#18.8 Example App: Temperature Converter

import tkinter as tk

def fahrenheit_to_degrees():
    try:
        fahrenheit = float(user_entry.get())
        degree = (5/9)*(fahrenheit - 32)
        result_label["text"] = f"{degree:.2f} {"\N{DEGREE CELSIUS}"}"
    except ValueError:
        result_label["text"] = "Wrong entry, enter a valid temperature value"

window = tk.Tk()

window.title("Temperature Converter App")
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0,1,2], minsize=50, weight=1)

frame_entry = tk.Frame(master=window)
user_entry = tk.Entry(master=frame_entry)
entry_label = tk.Label(master=frame_entry, text="\N{DEGREE FAHRENHEIT}")
user_entry.grid(row=0, column=0, sticky="e")
entry_label.grid(row=0, column=1, sticky="w")

button_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_degrees)
result_label = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frame_entry.grid(row=0, column=0, padx=10)
button_convert.grid(row=0, column=1, padx=10)
result_label.grid(row=0, column=2, padx=10)

window.mainloop()
