#18. Graphical User Interfaces
#18.1 Add GUI Elemnts With EasyGUI
# Graceful exit of the program once user presses cancle.
import easygui as gui

path = gui.fileopenbox(title="Select a file")

if path is None:
    exit()

    
