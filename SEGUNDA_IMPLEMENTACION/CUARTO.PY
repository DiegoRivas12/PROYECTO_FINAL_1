import os
import matplotlib.pyplot as plt

def process_sentiment_files(directory):
    sentiment_data = {}
    for filename in os.listdir(directory):
        if filename.endswith("_sentimiento.txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()
                sentiment_data[filename] = data
    return sentiment_data

def gender_bias_analysis(sentiment_data):
    gender_count = {"Femenino": 0, "Masculino": 0, "Desconocido": 0}
    for filename, data in sentiment_data.items():
        if "femenino" in filename.lower():
            gender_count["Femenino"] += 1
        elif "masculino" in filename.lower():
            gender_count["Masculino"] += 1
        else:
            gender_count["Desconocido"] += 1
    return gender_count

def plot_gender_bias(results):
    genders = list(results.keys())
    counts = list(results.values())

    plt.figure(figsize=(8, 6))
    plt.bar(genders, counts, color=['blue', 'orange', 'green'])
    plt.xlabel('Género')
    plt.ylabel('Cantidad')
    plt.title('Sesgo de género en análisis de sentimiento')
    plt.show()

def save_gender_bias_results(directory, results):
    output_path = os.path.join(directory, "analisis_sesgo_genero.txt")
    with open(output_path, "w", encoding="utf-8") as file:
        for gender, count in results.items():
            file.write(f"{gender}: {count}\n")

# Directorio que contiene los archivos de análisis de sentimientos
sentimientos_directory = "analisis_sentimientos"

# Procesar los archivos de sentimientos y obtener los datos
sentiment_data = process_sentiment_files(sentimientos_directory)

# Analizar sesgo de género en los datos
gender_bias_results = gender_bias_analysis(sentiment_data)

# Guardar los resultados del análisis de sesgo de género
output_directory = "resultados_sesgo_genero"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
save_gender_bias_results(output_directory, gender_bias_results)

# Graficar el sesgo de género
plot_gender_bias(gender_bias_results)
