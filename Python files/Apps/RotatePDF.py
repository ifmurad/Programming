import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

# 1. Display a file selection dialog for opening a PDF file.
input_path = gui.fileopenbox(
    title="Select a PDF to rotate...",
    default="*.pdf"
)

# 2. If the user cancels the dialog, then exit the program.
if input_path is None:
    exit()

# 3. Let the user select one of '90', '180' or '270' degrees to rotate the PDF pages.
choices = ("90", "180", "270")
degrees = None
while degrees is None:
    degrees = gui.buttonbox(
        msg = "Rotate the PDF clockwise by how many degrees?",
        title = "Choose rotation...",
        choices = choices,
        )
degrees = int(degrees)

# 4. Display a file selection dialog for saving the rotated PDF.
save_title = "Save the rotated PDF as..."
file_type = "*.pdf"
output_path = gui.filesavebox(title=save_title, default=file_type)

# 5. If the user tries to save with the same name as the input file:
while input_path == output_path:
    # - Alert the user with a message box that this is not allowed.
    gui.msgbox(msg="Cannot overwrite original file!")
    # - Return to step 4.
    output_path = gui.filesavebox(title=save_title, default=file_type)

# 6. If the user cancels the file save dialog, then exit the program.
if output_path is None:
    exit()

# 7. Perform the page rotation:
#     - Open the selected PDF.
input_file = PdfFileReader(input_path)
output_pdf = PdfFileWriter()

#     - Rotate all of the pages.
for page in input_file.pages:
    page = page.rotateClockwise(degrees)
    output_pdf.addPage(page)

#     - Save the rotated PDF to the selected file.
with open(output_path, "wb") as output_file:
    output_pdf.write(output_file)
