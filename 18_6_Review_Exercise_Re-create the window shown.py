#18.  Graphical User Interfaces
#18.6 Review Exercise: Re-create the window shown using the techniques you've learned so far
#     You may use any geometry manager you like

import tkinter as tk

# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Address Entry Form")

# Create a new frame `frm_form` to contain the Label
# and Entry widgets for entering address information.
frm_form = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
frm_form.pack()

# Create the Label and Entry widgets for "First Name"
lbl_first_name = tk.Label(master=frm_form, text="First Name:")
ent_first_name = tk.Entry(master=frm_form, width=50)
# Use the grid() geometry manager to place the Label and Entry widgets in the first and second columns of the first row of the grid
lbl_first_name.grid(row=0, column=0, sticky="e")
ent_first_name.grid(row=0, column=1)

# Create the Label and Entry widgets for the "Last Name"
lbl_last_name = tk.Label(master=frm_form, text="Last Name:")
ent_last_name = tk.Entry(master=frm_form, width=50)
# Place the widgets in the second row of the grid
lbl_last_name.grid(row=1, column=0, sticky="e")
ent_last_name.grid(row=1, column=1)

# Create the Label and Entry widgets for "Address Line 1"
lbl_address_line_1 = tk.Label(master=frm_form, text="Address Line 1:")
ent_address_line_1 = tk.Entry(master=frm_form, width=50)
# Place the widgets in the third row of the grid
lbl_address_line_1.grid(row=2, column=0, sticky="e")
ent_address_line_1.grid(row=2, column=1)

# Create the Label and Entry widgets for "Address Line 2"
lbl_address_line_2 = tk.Label(master=frm_form, text="Address Line 2:")
ent_address_line_2 = tk.Entry(master=frm_form, width=50)
# Place the widgets in the third row of the grid
lbl_address_line_2.grid(row=3, column=0, sticky="e")
ent_address_line_2.grid(row=3, column=1)

# Create the Label and Entry widgets for "City"
lbl_city = tk.Label(master=frm_form, text="City:")
ent_city = tk.Entry(master=frm_form, width=50)
# Place the widgets in the third row of the grid
lbl_city.grid(row=4, column=0, sticky="e")
ent_city.grid(row=4, column=1)

# Create the Label and Entry widgets for "State/Province"
lbl_state = tk.Label(master=frm_form, text="State/Province:")
ent_state = tk.Entry(master=frm_form, width=50)
# Place the widgets in the third row of the grid
lbl_state.grid(row=5, column=0, sticky="e")
ent_state.grid(row=5, column=1)

# Create the Label and Entry widgets for "Postal Code"
lbl_postal_code = tk.Label(master=frm_form, text="Postal Code:")
ent_postal_code = tk.Entry(master=frm_form, width=50)
# Place the widgets in the third row of the grid
lbl_postal_code.grid(row=6, column=0, sticky="e")
ent_postal_code.grid(row=6, column=1)

# Create the Label and Entry widgets for "Country"
lbl_country = tk.Label(master=frm_form, text="Country:")
ent_country = tk.Entry(master=frm_form, width=50)
# Place the widgets in the third row of the grid
lbl_country.grid(row=7, column=0, sticky="e")
ent_country.grid(row=7, column=1)

# Create a new frame `frm_buttons` to contain the Submit and Clear buttons. This frame fills the whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame(master=window)
frm_buttons.pack(fill=tk.X, padx=5, pady=5)

# Create the "Submit" button and pack it to the right side of `frm_buttons`
btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, pady=10)

# Create the "Clear" button and pack it to the right side of `frm_buttons`
btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, padx=10, pady=10)

# Start the application
window.mainloop()

