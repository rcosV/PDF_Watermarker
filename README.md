# PDF_Watermarker

This script applies a watermark to each page of a specified PDF document using the PyPDF2 library.

## How It Works

The script takes the name of a PDF file as a command-line argument and applies a watermark to each page of the document, saving the result as a new file with a prefix `watermarked_`.

## Requirements

- Python 3
- PyPDF2 library

## Installation

Install the PyPDF2 library using pip:

```bash
pip install PyPDF2

Usage
After installation, run the script from the command line by passing the name of the PDF you want to watermark:

python watermark.py your-pdf-file.pdf

Replace your-pdf-file.pdf with the actual file name of the PDF you wish to watermark.

Customization
You can customize the watermark by replacing the "wtr.pdf" file with your own watermark file in the script.

Contributions
Contributions are welcome. Please ensure you follow the code of conduct and contribution guidelines.