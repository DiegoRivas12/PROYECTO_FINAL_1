import os
from PIL import Image
import random
import pandas as pd
# Directorio donde se guardaron las capturas de pantalla
screenshot_dir = 'screenshots'

# Crear una lista para almacenar los píxeles recopilados
pixels = []

# Función para recopilar los píxeles
def collect_pixels(image_path):
    try:
        # Abrir la imagen usando PIL
        image = Image.open(image_path)
        
        # Convertir la imagen a escala de grises para facilitar la detección de colores blancos
        gray_image = image.convert('L')
        
        # Definir un umbral para los píxeles blancos
        threshold = 200
        
        # Recorrer la imagen y recopilar píxeles no blancos
        for x in range(image.width):
            for y in range(image.height):
                pixel = gray_image.getpixel((x, y))
                if pixel < threshold:
                    pixels.append(image.getpixel((x, y)))
    
    except Exception as e:
        print(f'Error al procesar la imagen {image_path}: {str(e)}')

# Obtener la lista de archivos de imágenes en el directorio
image_files = [file for file in os.listdir(screenshot_dir) if file.endswith('.png')]

# Seleccionar aleatoriamente un número específico de imágenes
num_images_to_process = 10  # Número de imágenes a procesar (ajusta según sea necesario)
selected_images = random.sample(image_files, min(num_images_to_process, len(image_files)))

# Recopilar píxeles de las imágenes seleccionadas
for image_file in selected_images:
    image_path = os.path.join(screenshot_dir, image_file)
    collect_pixels(image_path)

# Seleccionar 3000 píxeles aleatorios de la lista recopilada
num_pixels_to_select = 3000
selected_pixels = random.sample(pixels, min(num_pixels_to_select, len(pixels)))

# Realizar normalización u otros procesamientos según sea necesario con los píxeles seleccionados
# por ejemplo, aplicar el modelo de color RGB y normalizarlos

# Continuación del código previo para seleccionar y procesar los píxeles

# Realizar el procesamiento adicional con los píxeles seleccionados
# Por ejemplo, podríamos calcular el promedio de los valores de los píxeles en cada canal RGB

# Obtener los canales RGB de los píxeles seleccionados
red_values = [pixel[0] for pixel in selected_pixels]
green_values = [pixel[1] for pixel in selected_pixels]
blue_values = [pixel[2] for pixel in selected_pixels]

# Calcular el promedio de cada canal
average_red = sum(red_values) / len(red_values)
average_green = sum(green_values) / len(green_values)
average_blue = sum(blue_values) / len(blue_values)

average_data = pd.DataFrame({
    'Average_Red': [average_red],
    'Average_Green': [average_green],
    'Average_Blue': [average_blue]
})

# Mostrar el nuevo DataFrame con los promedios de los canales RGB
print(average_data)
# Guardar los promedios en un archivo CSV llamado 'data.csv'
average_data.to_csv('data.csv', index=False)
# Imprimir los resultados de los promedios de cada canal RGB
print(f"Promedio del canal Rojo: {average_red}")
print(f"Promedio del canal Verde: {average_green}")
print(f"Promedio del canal Azul: {average_blue}")

# Continuar con cualquier otro análisis o procesamiento requerido con los píxeles seleccionados
# ...

