import PyPDF2
import sys

# Check if the user has provided a command-line argument
if len(sys.argv) < 2:
    print("Usage: python watermark.py your-pdf-file.pdf")
    sys.exit(1)

template_pdf = sys.argv[
    1
]  # Get the template PDF file name from the command-line argument

# Open the PDF files
template = PyPDF2.PdfReader(open(template_pdf, "rb"))
watermark = PyPDF2.PdfReader(open("wtr.pdf", "rb"))
output = PyPDF2.PdfWriter()

# Iterate through each page and apply the watermark
for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

# Write the output PDF to a file
with open(f"watermarked_{template_pdf}", "wb") as file:
    output.write(file)
