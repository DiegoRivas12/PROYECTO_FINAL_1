import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

def process_thesis_files(directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(file_path)
            # Guardar el texto en un archivo de texto separado
            text_file_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.txt")
            with open(text_file_path, "w", encoding="utf-8") as text_file:
                text_file.write(text)

# Directorio que contiene los archivos PDF
thesis_directory = "tesis"
# Directorio donde se guardarán los archivos de texto extraídos
output_folder = "resultados_texto"

# Procesar los archivos PDF y guardar el texto extraído en archivos de texto en el directorio especificado
process_thesis_files(thesis_directory, output_folder)
