# extract_doc_info.py

from pathlib import Path
from PyPDF2 import PdfFileReader
import os, sys

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information

if __name__ == '__main__':
    path_dir = Path(sys.argv[1])
    list_pdf_files = [path_dir / book for book in os.listdir(path_dir) if book.endswith('pdf')]
    for count, file_ in enumerate(list_pdf_files):
        print(f'Book: {file_}, number: {count + 1}')
        extract_information(file_)
