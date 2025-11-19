#18. Graphical User Interfaces
#18.7 Making Your Applications Interactive

# Since tkinter automatically appends an event object to an events_list whenever an event occurs in the loop,
# Let us create an infinite loop that continually checks if any event objects are in the events_list:
import tkinter as tk

# Assume that this lis gets updated automatically
events_list = []

#Run the event loop
while True:
    # If events_list is empty, then no events have occured and you
    # can skip to the next iteration of the loop
    if events_list = []:
        continue

    # If execution reaches this point, then at least one
    # event object is in events_list
    event = events_list[0]

