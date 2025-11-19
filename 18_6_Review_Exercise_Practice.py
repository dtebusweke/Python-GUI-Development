import tkinter as tk

window = tk.Tk()

frame_main = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=1 )
frame_main.pack(fill=tk.BOTH, expand=True)

button_submit = tk.Button(master = window, text="Submit")
button_submit.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

button_clear = tk.Button(master = window, text="Clear")
button_clear.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)


window.mainloop()
