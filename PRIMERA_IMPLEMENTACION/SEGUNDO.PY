import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL de la página principal de la tecnología educativa
url = 'https://www.unsa.edu.pe/'

# Realizar la solicitud GET a la página
response = requests.get(url)

if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todos los enlaces (<a>) en la página
    links = soup.find_all('a')
    
    # Lista para almacenar los enlaces permitidos
    allowed_links = []
    
    for link in links:
        href = link.get('href')
        absolute_link = urljoin(url, href)  # Convertir a URL absoluta
        
        # Realizar verificación con el archivo robots.txt
        robots_url = urljoin(url, '/robots.txt')
        robots_response = requests.get(robots_url)
        
        if robots_response.status_code == 200:
            # Verificar si el enlace está permitido por robots.txt
            if absolute_link not in robots_response.text:
                allowed_links.append(absolute_link)
        else:
            print('Error al acceder al archivo robots.txt')
    
    # Mostrar los enlaces permitidos
    for allowed_link in allowed_links:
        print(allowed_link)
else:
    print('Error al acceder a la página:', response.status_code)
