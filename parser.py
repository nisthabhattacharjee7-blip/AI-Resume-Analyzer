from pyPDF2  import PDFReader
def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PDFReader(pdf_file)

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text 
    return text