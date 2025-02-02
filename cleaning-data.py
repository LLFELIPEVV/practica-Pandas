import pandas as pd

# La limpieza de datos es un proceso importante en la ciencia de datos, ya que los datos crudos pueden contener errores, duplicados o valores faltantes.
# Los datos erroneos podrian ser:
"""
- Celdas vacias
- Datos en formato incorrecto
- Datos equivocados
- Duplicados
"""
# Limpieza de celdas vacias
# Las celdas vacias pueden dar potencialmente un resultado erroneo al analizar los datos.
print("Limpieza de celdas vacias")

# Eliminar filas
# Una de las formas de lidiar con las celdas vacias es eliminar las filas que las contienen.
# El metodo dropna() devuelve un nuevo DataFrame y no cambia el original.
df = pd.read_csv("data.csv")
new_df = df.dropna()

print("Eliminando filas")
print(new_df.to_string())

# Eliminando las filas en el DataFrame original
# El argumento inplace = True hace que el cambio sea efectivo en el DataFrame original.
df.dropna(inplace=True)

print("Eliminando filas en el DataFrame original")
print(df.to_string())

# Reemplazar valores vacios en todas las columnas
# Podemos reemplazar los valores vacios por un numero, string o mediana.
# El metodo fillna() permite reemplazar los valores vacios.
df = pd.read_csv("data.csv")
df.fillna(130, inplace=True)

print("Reemplazando valores vacios con el numero 30")
print(df.to_string())

# Reemplazar valores vacios en una columna especifica
df = pd.read_csv("data.csv")
df["Calories"].fillna(130, inplace=True)

print("Reemplazando valores vacios de la columna Calories")
print(df.to_string())

# Reemplazar valores vacios usando la media, mediana o moda
# La media "mean()" es el valor promedio, la mediana "median()" es el valor en el medio y la moda "mode()" es el valor que mas se repite.
df = pd.read_csv("data.csv")
x = df["Calories"].mean()
df["Calories"] = df["Calories"].fillna(x)

print("Reemplazando valores vacios con la media")
print(df.to_string())

# Reemplazar con la mediana
df = pd.read_csv("data.csv")
x = df["Calories"].median()
df["Calories"] = df["Calories"].fillna(x)

print("Reemplazando valores vacios con la mediana")
print(df.to_string())

# Reemplazar con la moda
df = pd.read_csv("data.csv")
x = df["Calories"].mode()[0]
df["Calories"] = df["Calories"].fillna(x)

print("Reemplazando valores vacios con la moda")
print(df.to_string())

# Limpieza de datos con formato incorrecto
# Los datos con formato incorrecto pueden dificultar o imposibilitar el analisis de los datos.
# Hay dos posibles soluciones eliminar las filas o cambiar el formato de toda la columna.
print()
print("Limpieza de datos con formato incorrecto")

# Convirtiendo datos a un formato correcto
df = pd.read_csv("data-2.csv")
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

print("Convirtiendo datos a un formato correcto")
print(df.to_string())

# Eliminando las filas con datos vacios
df.dropna(subset=["Date"], inplace=True)

print("Eliminando las filas con datos vacios")
print(df.to_string())
