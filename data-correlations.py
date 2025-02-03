import pandas as pd

# El metodo corr() calcula la relacion entre cada columna de su conjunto de datos.
# El numero que aparece indica la relacion. El numero que mas se acerca a 1 o -1 indica una relacion muy fuerte.
# El metodo corr() ignora las columnas no numericas.
# Se debe tener al menos -0.6 o 0.6 para considerarse una buena relacion.
print("Correlacion entre las columnas")

# Mostrando la relacion entre columnas
df = pd.read_csv("data.csv")

print(df.corr())
