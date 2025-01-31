import pandas as pd

# Pandas permite analizar grandes cantidades de datos y sacar conclusiones.
# Principalmente funciona para limpiar datos.
# Usando pandas
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print("Usando pandas: ")
print(myvar)

# Comprobando la version de pandas
print(f"Version de pandas: {pd.__version__}")

# Pandas Series
# Una serie en pandas es como una columna en una tabla.
# Una serie es una matriz unidimensional que contiene datos de cualquier tipo.
print()
print("Pandas Series")

# Creando una serie con pandas a partir de una lista
a = [1, 7, 2]
myvar = pd.Series(a)
print("Creando una serie con pandas:")
print(myvar)

# Etiquetas
# Si no se especifica una etiqueta, entonces el valor se toma como etiqueta.
# La etiqueta en la primera fila de la serie se toma como la etiqueta 0, la segunda como 1, etc.
print(f"Etiqueta 0: {myvar[0]}")

# Creando una etiqueta
# Esto se puede cambiar con el argumento index.
myvar = pd.Series(a, index=["x", "y", "z"])

print("Creando una etiqueta:")
print(myvar)
print(f"Etiqueta y: {myvar['y']}")  # 7

# Objetos de clave/valor como series
# Se puede usar el argumento de clave/valor para crear una serie.
# Las claves se convierten en las etiquetas.
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)

print("Objetos de clave/valor como series:")
print(myvar)

# Seleccionando datos para crear una serie
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index=["day1", "day2"])

print("Seleccionando datos para crear una serie:")
print(myvar)

# DataFrames
# Un DataFrame es una matriz 2D que contiene datos de varias series.
# Un DataFrame es un objeto de datos bidimensional con columnas de diferentes tipos, como números, cadenas, listas, etc.
# Creando un DataFrame a partir de dos series
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print("Creando un DataFrame a partir de dos series:")
print(myvar)

# DataFrames en Pandas
# Un Pandas DataFrame es una estructura de datos bidimensional, como una matriz bidimensional o una tabla con filas y columnas.
print()
print(f"DataFrames en Pandas")

# Creando un Pandas DataFrame simple
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print("Creando un Pandas DataFrame simple:")
print(df)

# Localizar Filas
# Podemos usar el método loc para localizar una fila específica.
# Usamos el nombre de la fila para localizarlo.
# Localizando la fila 0. Esto devuelve una Serie.
print("Localizando la fila 0:")
print(df.loc[0])

# Localizando las filas 0 y 1. Esto devuelve un DataFrame.
print("Localizando las filas 0 y 1:")
print(df.loc[[0, 1]])

# Indices con nombre
# Con el index argumento podemos nombrar nuestras filas.
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print("Indices con nombre:")
print(df)

# Localizando indices con nombre
print("Localizando indices con nombre:")
print(df.loc["day2"])
