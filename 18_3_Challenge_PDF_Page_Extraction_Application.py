#18. Graphical User Interface
#18.3 Challenge: PDF Page Extraction Application
from PyPDF2 import PdfFileWriter, PdfFileReader
import easygui as gui

#1. In this challenge, you’ll use EasyGUI to write a GUI application for extracting pages from a PDF file.
#   Here’s a detailed plan for the application:
#1.  Ask the user to select a PDF file to open.

pdf_open_path = gui.fileopenbox(
    title="Enter file to open",
    default="*.pdf"
    )

#2. If no PDF file is chosen, then exit the program.
if pdf_open_path is None:
    exit()

#3. Ask for a starting page number.
page_start = gui.enterbox(
    title="Starting page number:",
    msg="Enter stating page number:"
    )

#4. If the user doesn’t enter a starting page number, then exit the program.
if page_start is None:
    exit()

#5. Valid page numbers are positive integers. If the user enters an invalid page number:
#  • Warn the user that the entry is invalid.
#  • Return to step 3.

reader=PdfFileReader(pdf_open_path)
num_pages = reader.getNumPages()

while(int(page_start) > num_pages or int(page_start)==0 or not page_start.isdigit()):
    msg = gui.msgbox(
        title="Warning!",
        msg="Invalid input. Input number should be > 0 and an int"
        )
    page_start = gui.enterbox(
        title="Starting page number:",
        msg="Enter stating page number:"
        )
    if page_start is None:  # exit on "Cancel"
        exit()

#6. Ask for an ending page number.
page_end = gui.enterbox(
    title="End page number:",
    msg="Enter end page number:"
    )

#7. If the user doesn’t enter an ending page number, then exit the program.
if page_end is None:
    exit()

#8. If the user enters an invalid page number:
#    • Warn the user that the entry is invalid.
#    • Return to step 6.
while(not page_end.isdigit() or int(page_end)=='0' or int(page_end) <= int(page_start) or int(page_end) > num_pages):
    msg = gui.msgbox(
        title="Warning!",
        msg="Invalid input. Input number should be > 0 and an int"
        )
    if msg is None:
        exit()
    page_end = gui.enterbox(
        title="End page number:",
        msg="Enter end page number:"
        )

#9. Ask for the location to save the extracted pages.
pdf_save_path = gui.filesavebox(
    title="Enter filee name of the extracted pages to be saved",
    default="*.pdf"
    )

#10. If the user doesn’t select a save location, then exit the program.
if pdf_save_path is None:
    exit()

#11. If the chosen save location is the same as the input file path:
#   • Warn the user that they can’t overwrite the input file.
#   • Return to step 9.
while pdf_save_path == pdf_open_path:
    msg1 = gui.msgbox(
        title="Warning!",
        msg="Invalid file name, file name for extracted files should not be the same as the original file name as this shall override the original file name"
        )
    pdf_save_path = gui.filesavebox(
        title="Enter filee name of the extracted pages to be saved",
        default="*.pdf"
        )
#12. Perform the page extraction:
#  • Open the input PDF file.
#  • Write a new PDF file containing only the pages in the selected page range.
reader = PdfFileReader(pdf_open_path)
writer = PdfFileWriter()

for i in range(int(page_start)-1, int(page_end)):
    page = reader.getPage(i)
    writer.addPage(page)

with open(pdf_save_path, 'wb') as output_file:
    writer.write(output_file)


    
