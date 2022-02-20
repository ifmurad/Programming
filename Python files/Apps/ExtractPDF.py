import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

# 1. Ask the user to select a PDF file to open.
input_path = gui.fileopenbox(
    title = "Select PDF to extract from...",
    default = "*.pdf"
)

# 2. If no PDF file is chosen, exit the program.
if input_path is None:
    exit()

# 3. Ask for a starting page number.
starting_page = gui.enterbox(
    msg = "What is starting page number?",
    title = "Choose starting page number..."
)

# 4. If the user does not enter a starting page number, exit the program.
if starting_page is None:
    exit()
n = 0
try:
    starting_page = int(starting_page)
except ValueError:
    n+=1

input_file = PdfFileReader(input_path)

# 5. Valid page numbers are positive integers. If the user enters an invalid page number:
while n == 1 or starting_page <= 0 or starting_page > input_file.getNumPages():
    #    - Warn the user that the entry is invalid.
    gui.msgbox(msg = "The entry is ivalid!")
    #    - Return to step 3.
    # 3. Ask for a starting page number.
    starting_page = gui.enterbox(
        msg = "What is starting page number?",
        title = "Choose starting page number..."
        )
    n = 0
    # 4. If the user does not enter a starting page number, exit the program.
    if starting_page is None:
        exit()
    try:
        starting_page = int(starting_page)
    except ValueError:
        n+=1

# 6. Ask for an ending page number.
ending_page = gui.enterbox(
    msg = "What is ending page number?",
    title = "Choose ending page number..."
)

# 7. If the user does not enter an ending page number, exit the program.
if ending_page is None:
    exit()
try:
    ending_page = int(ending_page)
except ValueError:
    n+=1

# 8. If the user enters an invalid page number:
while n == 1 or ending_page <= starting_page or ending_page > input_file.getNumPages():
    #    - Warn the user that the entry is invalid.
    gui.msgbox(msg = "The entry is ivalid!")
    #    - Return to step 6.
    # 6. Ask for an ending page number.
    ending_page = gui.enterbox(
        msg = "What is ending page number?",
        title = "Choose ending page number..."
        )
    n = 0
    # 7. If the user does not enter an ending page number, exit the program.
    if ending_page is None:
        exit()
    try:
        ending_page = int(ending_page)
    except ValueError:
        n+=1

# 9. Ask for the location to save the extracted pages.
save_title = "Save the extracted pages"
file_type = "*.pdf"
output_path = gui.filesavebox(title = save_title, default = file_type)

# 10. If the user does not select a save location, exit the program.
if output_path is None:
    exit()

# 11. If the chosen save location is the same as the input file path:
while output_path == input_path:
    #    - Warn the user that they can not overwrite the input file.
    gui.msgbox(msg = "Cannot overwrite the original file")
    #    - Return to step 9.
    output_path = gui.filesavebox(title = save_title, default = file_type)
    if output_path is None:
        exit()

# 12. Perform the page extraction:
#    - Open the input PDF file.

output_pdf = PdfFileWriter()

#    - Write a new PDF file containing only the pages in the selected page range.
for n in range(starting_page-1, ending_page):
    page = input_file.getPage(n)
    output_pdf.addPage(page)

with open(output_path, "wb") as output_file:
    output_pdf.write(output_file)
