import os
from pypdf import PdfWriter
path = input("Enter the path of the file : ")
os.chdir(f'{path}')
merger = PdfWriter()
files = os.listdir()
for file in files:
    merger.append(fileobj=file)
merger.write('Combined PDF.pdf')
merger.close()