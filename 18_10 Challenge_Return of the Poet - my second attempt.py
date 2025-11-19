#18   Graphical User Interface
#18.10 Challenge: Return of the Poet
# My second attempt after checking solution and comparing it to my first attempt

import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import random

#Create the window
window = tk.Tk()
window.title('Make your own poem!')

#first_frame = tk.Frame(master=window)
#first_frame.grid(row=0, column)

first_label = tk.Label(master=window, text="Enter your favorite words, separated by commas.")
first_label.pack(padx=5, pady=5)

frame_entries = tk.Frame(master=window)
frame_entries.pack(padx=5)

nouns_label = tk.Label(master=frame_entries, text="Nouns:")
nouns_label.grid(row=0, column=0, sticky='e')
nouns_entry = tk.Entry(master=frame_entries, width=100)
nouns_entry.grid(row=0, column=1, sticky='w', padx=5)

verbs_label = tk.Label(master=frame_entries, text="Verbs:")
verbs_label.grid(row=1, column=0, sticky='e')
verbs_entry = tk.Entry(master=frame_entries, width=100)
verbs_entry.grid(row=1, column=1, sticky='w', padx=5)

adjs_label = tk.Label(master=frame_entries, text="Adjectives:")
adjs_label.grid(row=2, column=0, sticky='e')
adjs_entry = tk.Entry(master=frame_entries, width=100)
adjs_entry.grid(row=2, column=1, sticky='w', padx=5)

prp_label = tk.Label(master=frame_entries, text="Prepositions:")
prp_label.grid(row=3, column=0, sticky='e')
prp_entry = tk.Entry(master=frame_entries, width=100)
prp_entry.grid(row=3, column=1, sticky='w', padx=5)

adv_label = tk.Label(master=frame_entries, text="Adverbs:")
adv_label.grid(row=4, column=0, sticky='e')
adv_entry = tk.Entry(master=frame_entries, width=100)
adv_entry.grid(row=4, column=1, sticky='w', padx=5)

btn_gen = tk.Button(master=window, text='Generate', bg='#AED6F1')
btn_gen.pack(pady=10)

frm_results = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5, width=100, bg='#FEF9E7')
frm_results.pack(fill=tk.X, padx=5)

poem_lbl = tk.Label(master=frm_results, text='Your poem:', bg='#FEF9E7')
poem_lbl.pack(padx=5, pady=5)

result_label = tk.Label(master=frm_results, bg='#FEF9E7')
result_label.pack(padx=5)

save_btn = tk.Button(master=frm_results, text='Save to file', bg='#9FE2BF')
save_btn.pack(padx=5, pady=5)

def is_uniq(list_input):
    """Functions takes in a list, creates a new list, and then copies a word from the parameter list and adds it in the new list only if it is not there
       . Finally it compares the lengths of the two lists and returns TRUE or FALSE if the length is same or not"""
    new_list = []
    for word in list_input:
        if word not in new_list:
            new_list.append(word)
    return(len(list_input) == len(new_list))

def generate_poem():
    """Event handler function when the 'Generate' button is pressed"""
    nouns_user = nouns_entry.get().split(',')
    nouns_list = [word.strip().lower() for word in nouns_user]
    
    verbs_user = verbs_entry.get().split(',')
    verbs_list = [word.strip().lower() for word in verbs_user]
    
    adjs_user = adjs_entry.get().split(',')
    adjs_list = [word.strip().lower() for word in adjs_user]
    
    prp_user = prp_entry.get().split(',')
    prp_list = [word.strip().lower() for word in prp_user]

    adv_user = adv_entry.get().split(',')
    adv_list = [word.strip().lower() for word in adv_user]

    if not (is_uniq(nouns_list) and is_uniq(verbs_list) and is_uniq(adjs_list) and is_uniq(prp_list) and is_uniq(adv_list)):
        result_label['text'] = 'Wrong entry. Only enter unique words per each entery!'
        result_label['fg'] = 'red'
        return

    if(len(nouns_list)<3 or len(verbs_list)<3 or len(adjs_list)<3 or len(prp_list)<3 or len(adv_list)<1):
        result_label['text'] = 'Wrong entry. Enter the right number of words per entry!\nAt least: 3 nouns, 3 verbs, 3 adjectives, 3 prepositions and 1 adverb'
        result_label['fg'] = 'red'
        return

    article = ''
    if(adjs_list[0] in 'aeiou'):
        article = f"An {adjs_list[0]}"
    else:
        article = f"A {adjs_list[0]}"

    poem = f"{article} {nouns_list[0]}\n\n"
    poem = poem + f"A {adjs_list[0]} {nouns_list[0]} {verbs_list[0]} {prp_list[0]} the {adjs_list[1]} {nouns_list[1]}\n"
    poem = poem + f"{adv_list[0]}, the {nouns_list[0]} {verbs_list[1]}\n"
    poem = poem + f"the {nouns_list[1]} {verbs_list[2]} {prp_list[1]} a {adjs_list[2]} {nouns_list[2]}"

    result_label['text'] = poem
    result_label['fg'] = 'black'
    return

btn_gen['command'] = generate_poem

def save_file():
    file_path = asksaveasfilename(
        defaultextension = "*.txt",
        filetypes = [("Text files","*.txt"),("All other files","*.*")]
        )

    if not file_path:
        return
    with open(file_path,'w') as output_file:
        text = result_label['text']
        output_file.write(text)
    return
save_btn['command'] = save_file
    
window.mainloop()
