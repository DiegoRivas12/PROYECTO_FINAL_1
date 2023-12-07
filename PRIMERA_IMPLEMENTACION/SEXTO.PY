import pandas as pd
import numpy as np
from scipy.stats import f_oneway
#Este código simula la realización de un análisis de varianza (ANOVA) para verificar 
# si existen diferencias significativas en los canales de color RGB con respecto al género. 
# Puedes aplicar técnicas estadísticas similares para otras variables demográficas, 
# como la edad o el área de estudio, según tu conjunto de datos y objetivos de análisis.

# Cargar el archivo CSV 'data.csv' que contiene los promedios de los canales RGB
data = pd.read_csv('data.csv')

# Supongamos que tenemos datos demográficos adicionales para análisis (género, edad, área de estudio, etc.)
# Crear datos de ejemplo para estas variables demográficas
data['Genero'] = np.random.choice(['Masculino', 'Femenino'], size=len(data))
data['Edad'] = np.random.randint(18, 60, size=len(data))
data['Area_de_estudio'] = np.random.choice(['Ciencias', 'Arte', 'Tecnología', 'Negocios'], size=len(data))

# Realizar un análisis de varianza (ANOVA) para ver si hay diferencias significativas en los canales RGB según el género
anova_red = f_oneway(data[data['Genero'] == 'Masculino']['Average_Red'],
                     data[data['Genero'] == 'Femenino']['Average_Red'])

anova_green = f_oneway(data[data['Genero'] == 'Masculino']['Average_Green'],
                       data[data['Genero'] == 'Femenino']['Average_Green'])

anova_blue = f_oneway(data[data['Genero'] == 'Masculino']['Average_Blue'],
                      data[data['Genero'] == 'Femenino']['Average_Blue'])

# Imprimir los resultados de ANOVA para cada canal RGB
print("Resultados de ANOVA para el canal Rojo según género:", anova_red)
print("Resultados de ANOVA para el canal Verde según género:", anova_green)
print("Resultados de ANOVA para el canal Azul según género:", anova_blue)
