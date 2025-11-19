#18   Graphical User Interface
#18.9 Example App: Text Editor - Retry

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("Text Editor App")

def file_open():

    text_file = askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All other files","*.*")]
        )

    if text_file is None:
        return

    txt_area.delete("1.0", tk.END)

    with open(text_file, "r") as output_file:
        text = output_file.read()
        txt_area.insert(tk.END, text)
        window.title(f"Text Editor App - {text_file}")

def file_save():

    text_file = asksaveasfilename(
        defaultextension = "*.txt",
        filetypes=[("Text files", "*.txt"), ("All other files","*.*")]
        )

    if text_file is None:
        return

    with open(text_file, "w") as output_file:
        text = txt_area.get("1.0", tk.END)
        output_file.write(text)
        window.title(f"Text Editor App - {text_file}")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize = 800, weight=1)

frm_btns = tk.Frame(window)
btn_open = tk.Button(frm_btns, text="File Open", bg="#6495ED", command=file_open)
btn_save = tk.Button(frm_btns, text="Save As...", bg="#40E0D0", command=file_save)
btn_open.grid(row=0, column=0, padx=5, pady=5)
btn_save.grid(row=1, column=0, padx=5)

txt_area = tk.Text(window, bg="#fef9e7")

frm_btns.grid(row=0, column=0, sticky="ns")
txt_area.grid(row=0, column=1, sticky="nsew")


window.mainloop()
