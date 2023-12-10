import os
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def process_text_files(directory):
    text_data = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as text_file:
                text = text_file.read()
                text_data[filename] = text
    return text_data

def get_common_words(text):
    stop_words = set(stopwords.words('spanish'))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
    word_freq = Counter(filtered_words)
    return word_freq

def save_results(directory, results):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for filename, word_freq in results.items():
        output_file = os.path.join(directory, f"{os.path.splitext(filename)[0]}_frecuencia.txt")
        with open(output_file, "w", encoding="utf-8") as file:
            for word, frequency in word_freq.items():
                file.write(f"{word}: {frequency}\n")

# Directorio que contiene los archivos de texto
text_files_directory = "resultados_texto"

# Procesar los archivos de texto y obtener los datos de texto
text_data = process_text_files(text_files_directory)

# Obtener las palabras más comunes y guardar los resultados
results = {}
for filename, text in text_data.items():
    word_freq = get_common_words(text)
    results[filename] = word_freq

# Guardar los resultados en archivos de texto
output_directory = "frecuencia"
save_results(output_directory, results)
