#18. Graphical User Interfaces
#18.5 Working With Widgets
#Review Exercise

import tkinter as tk

#1. Try to re-create all the screenshots in this section without looking at the source code. If you get stuck, check the code and finish your re-creation. Then wait for ten or fifteen minutes and try again.

#2:
window = tk.Tk()

button = tk.Button(text='Click here', bg='white', fg='blue', width=50, height=25)
button.pack()

#window.mainloop()

#3:
entry_box = tk.Entry(width=40, bg='white', fg='black')
entry_box.insert(0, "What is your name?")
entry_box.pack()

window.mainloop()
