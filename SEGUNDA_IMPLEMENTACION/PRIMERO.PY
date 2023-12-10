import PyPDF2
import os

# Directorio que contiene los archivos PDF de las tesis
directory = 'directorio/de/las/tesis'

def extract_text_from_pdf(pdf_file):
    text = ''
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def process_thesis_files(directory):
    thesis_texts = {}
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(file_path)
            thesis_texts[filename] = text
    return thesis_texts

# Procesar archivos PDF de las tesis en el directorio dado
thesis_data = process_thesis_files(directory)

# thesis_data contendría un diccionario donde las claves son los nombres de archivo de las tesis
# y los valores son el texto extraído de los respectivos archivos PDF
