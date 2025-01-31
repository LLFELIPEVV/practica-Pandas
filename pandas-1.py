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
