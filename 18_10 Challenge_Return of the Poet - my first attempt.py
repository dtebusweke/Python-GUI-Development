#18   Graphical User Interface
#18.10 Challenge: Return of the Poet

# For this challenge, you’ll write a GUI application for generating poetry.
# This application is based on the poem generator from chapter 9.
# Visually, the application should look similar to this:
# You may use whichever geometry manager you like, but the application should do all of the following:
#   1. The user should be required to enter the correct number of words in each Entry widget:
#      • At least three nouns
#      • At least three verbs
#      • At least three adjectives
#      • At least three prepositions
#      • At least one adverb
#     If too few words are entered into any of the Entry widgets, then an error message should be displayed in the area
#     where the generated poem is shown.
#   2. The program should randomly choose three nouns, three adverbs, three adjectives, and three prepositions as well as
#      one adverb from the user input.
#   3. The program should generate the poem using the following template:
#      {A/An} {adj1} {noun1}
#       A {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
#      {adverb1}, the {noun1} {verb2}
#       the {noun2} {verb3} {prep2} a {adj3} {noun3}
#   4. The application must allow the user to export their poem to a file.
#   5. Bonus: Check that the user inputs unique words into each Entry widget. For example, if the user enters the same noun
#      into the noun Entry widget twice, then the application should display an error message when the user tries to
#      generate the poem.

import tkinter as tk
import random
from tkinter.filedialog import asksaveasfilename
import copy

#Initiation of main window
window = tk.Tk()
window.title("Make Your Own Poem!")
window.columnconfigure(0, minsize=600, weight=1)
window.rowconfigure(3, minsize=200, weight=1)

#Title label
lbl_title = tk.Label(master=window, text="Enter your favorite words, separated by commas.")
lbl_title.grid(row=0, column=0, padx=5, pady=5)

# Generate Button event handling
def generate():
    #Capture user input and store it lists
    nouns_list = str(entry_nouns.get()).split(',')
    verbs_list = str(entry_verbs.get()).split(',')
    adj_list   = str(entry_adj.get()).split(',')
    prp_list   = str(entry_prp.get()).split(',')
    adv_list   = str(entry_adv.get()).split(',')

    adj_list_1_copy = copy.deepcopy(adj_list[0])
    if adj_list[0][0] in ['a','e','i','o','u']:
        adj_list[0] = f"An {adj_list[0]}"

    #Assign the result to the label
    result_text = f"{adj_list[0]} {nouns_list[0]}\n{adj_list_1_copy} {nouns_list[0]} {verbs_list[0]} {prp_list[0]} the {adj_list[1]} {nouns_list[1]}\n{adv_list[0]}, the {nouns_list[0]} {verbs_list[1]}\nthe {nouns_list[1]} {verbs_list[2]} {prp_list[1]} {adj_list[2]} {nouns_list[2]}"
    
    result_lbl["text"] = result_text

def save_as():
    text_file = asksaveasfilename(
        defaultextension = "*.txt",
        filetypes = [("Text file", "*.txt"),("All other files", "*.*")]
                                 )

    if not text_file:
        return

    with open(text_file, 'w') as output_file:
        text = result_lbl["text"]
        output_file.write(text)

#Frame to house entry widgets and their lables
frm_entry = tk.Frame(master=window)
frm_entry.grid(row=1, column=0, padx=5, pady=5)

lbl_nouns = tk.Label(master=frm_entry, text="Nouns:")
lbl_nouns.grid(row=0, column=0, sticky="e")
entry_nouns = tk.Entry(master=frm_entry, width=100)
entry_nouns.grid(row=0, column=1, padx=5, sticky="e")

lbl_verbs = tk.Label(master=frm_entry, text="Verbs:")
lbl_verbs.grid(row=1, column=0, sticky="e")
entry_verbs = tk.Entry(master=frm_entry, width=100)
entry_verbs.grid(row=1, column=1,padx=5, sticky="e")

lbl_adj = tk.Label(master=frm_entry, text="Adjectives:")
lbl_adj.grid(row=2, column=0, sticky="e")
entry_adj = tk.Entry(master=frm_entry, width=100)
entry_adj.grid(row=2, column=1,padx=5, sticky="e")

lbl_prp = tk.Label(master=frm_entry, text="Prepositions:")
lbl_prp.grid(row=3, column=0, sticky="e")
entry_prp = tk.Entry(master=frm_entry, width=100)
entry_prp.grid(row=3, column=1,padx=5, sticky="e")

lbl_adv = tk.Label(master=frm_entry, text="Adverbs:")
lbl_adv.grid(row=4, column=0, sticky="e")
entry_adv = tk.Entry(master=frm_entry, width=100)
entry_adv.grid(row=4, column=1, padx=5, sticky="e")
    
#Generate button
btn_gen = tk.Button(master=window, text="Generate", bg="#40E0D0", command=generate)
btn_gen.grid(row=2, column=0, pady=5)

# Results label and Save button

result_frm = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5, bg='#FEF9E7')
result_frm.grid(row=3, column=0, sticky="nsew", padx=5, pady=5, ipady=10, ipadx=5)

result_lbl = tk.Label(master=result_frm, text="Generated poem will appear here!!", bg='#FEF9E7')
result_lbl.pack()

btn_save = tk.Button(master=result_frm, text="Save to File", bg="#9FE2BF", command=save_as)
btn_save.pack(side=tk.BOTTOM, pady=5)

#Continously run the app
window.mainloop()



