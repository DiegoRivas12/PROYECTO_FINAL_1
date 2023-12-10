import os
from textblob import TextBlob

def process_text_files(directory):
    text_data = {}
    for filename in os.listdir(directory):
        if filename.endswith("_frecuencia.txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as text_file:
                text = text_file.read()
                text_data[filename] = text
    return text_data

def analyze_sentiment(text_data):
    sentiment_results = {}
    for filename, text in text_data.items():
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = "Positivo"
        elif polarity < 0:
            sentiment = "Negativo"
        else:
            sentiment = "Neutro"
        sentiment_results[filename] = sentiment
    return sentiment_results

def save_sentiment_results(directory, results):
    for filename, sentiment in results.items():
        # Crear el nuevo nombre de archivo sin '_frecuencia'
        output_filename = filename.replace("_frecuencia.txt", "_sentimiento.txt")
        output_path = os.path.join(directory, output_filename)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(f"{filename}: {sentiment}\n")

# Directorio que contiene los archivos de frecuencia
frecuencia_directory = "frecuencia"

# Procesar los archivos de texto y obtener los datos
text_data = process_text_files(frecuencia_directory)

# Analizar el sentimiento de los textos
sentiment_results = analyze_sentiment(text_data)

# Guardar los resultados del análisis de sentimiento en archivos separados
output_directory = "analisis_sentimientos"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
save_sentiment_results(output_directory, sentiment_results)
