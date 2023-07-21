from PyPDF2 import PdfWriter, PdfReader
from pdf2image import convert_from_path
import fitz

pdffile = "/home/farid/pdfs/9.pdf"
# writer = PdfWriter()

# reader = PdfReader(fname)
# page = reader.pages[0]
# writer.add_page(page)
# with open("CombinedFirstPages.pdf", "wb") as output:
#     writer.write(output)

# pages = convert_from_path("CombinedFirstPages.pdf", 500)
# pages[0].save('hasil.jpg', 'JPEG')

# pdffile = "infile.pdf"
doc = fitz.open(pdffile)
page = doc.load_page(0)  # number of page
pix = page.get_pixmap()
output = "outfile.png"
pix.save(output)
doc.close()