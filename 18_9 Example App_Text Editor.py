#18. Graphical User Interfaces
#18.9 Example App: Text Editor

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing"""
    #1
    filepath = askopenfilename(
        filetypes = [("Text files", "*.txt"),("Files", "*.*")]
        )

    #2
    if not filepath:
        return

    #3
    txt_edit.delete("1.0",tk.END)

    #4
    with open(filepath, "r") as output_file:
        text = output_file.read()
        txt_edit.insert(tk.END, text)

    #5
    window.title(f"Simple Text Editor APP - {filepath}")

def save_file():
    """Save the current file as a new file."""
    #1
    filepath = asksaveasfilename(
        defaultextension = "txt", filetypes = [("Text files","*.txt") , ("Other files","*.*")]
        )

    #2
    if not filepath:
        return
    
    #3
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)

    #4
    window.title(f"Simple Text Editor - {filepath}")
        
# 1
window = tk.Tk()
window.title("Simple Text Editor")

# 2
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1) # avoid changing width of column 0

# 3
txt_edit = tk.Text(window, bg="#FEF9E7")
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", bg="#40E0D0", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", bg="#6495ED", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
