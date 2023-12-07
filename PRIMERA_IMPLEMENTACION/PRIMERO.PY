import requests
from bs4 import BeautifulSoup

# URL de la página principal de la tecnología educativa
url = 'https://www.unsa.edu.pe/'

# Realizar la solicitud GET a la página
response = requests.get(url)

if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todos los enlaces (<a>) en la página
    links = soup.find_all('a')
    
    # Mostrar los enlaces encontrados
    for link in links:
        print(link.get('href'))
else:
    print('Error al acceder a la página:', response.status_code)