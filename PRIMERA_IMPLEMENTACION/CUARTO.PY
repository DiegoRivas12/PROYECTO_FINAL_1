import os
from selenium import webdriver
import csv

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Para ejecutar en modo sin cabeza (sin abrir una ventana)
driver = webdriver.Chrome(options=options)

# Crear una carpeta para almacenar las capturas de pantalla si no existe
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Leer los enlaces desde el archivo CSV
with open('pages.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Saltar la fila del encabezado si existe
    for row in reader:
        link = row[0]  # Obtener el enlace de la fila
        
        try:
            # Abrir el enlace en el navegador
            driver.get(link)
            
            # Tomar una captura de pantalla y guardar en la carpeta "screenshots"
            screenshot_name = link.split('/')[-1] + '.png'  # Nombre del archivo de la captura de pantalla
            screenshot_path = os.path.join('screenshots', screenshot_name)
            driver.save_screenshot(screenshot_path)
            print(f'Se capturó la pantalla de {link} en {screenshot_path}')
        
        except Exception as e:
            print(f'Error al capturar la pantalla de {link}: {str(e)}')

# Cerrar el navegador al finalizar
driver.quit()
