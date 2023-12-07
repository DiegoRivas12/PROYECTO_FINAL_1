from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
# Cargar el archivo CSV 'data.csv' que contiene los promedios de los canales RGB
data = pd.read_csv('data.csv')

# Dividir el conjunto de datos en características (X) y la variable objetivo (y)
X = data[['Average_Green', 'Average_Blue']]
y = data['Average_Red']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
predictions = model.predict(X_test)

# Evaluar el rendimiento del modelo
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Mostrar métricas de rendimiento
print("Error cuadrático medio:", mse)
print("Coeficiente de determinación (R2 score):", r2)
