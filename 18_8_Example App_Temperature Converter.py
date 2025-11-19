#18. Graphical User Interfaces
#18.8 Example App: Temperature Converter

import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value from Fahrenheit to Celcius and insert the result into lbl_result."""
    fahrenheit = entry_temperature.get()
    celsius = (5/9)*(float(fahrenheit) - 32)
    lbl_result["text"] = f"{celsius:.2f} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Temperature Converter")

frm_entry          = tk.Frame(master=window)
entry_temperature  = tk.Entry(master=frm_entry, width=10)
lbl_temp           = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
entry_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, padx=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()
