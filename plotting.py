import pandas as pd
import matplotlib.pyplot as plt

# Se pueden graficar diagramas usando el modulo pyplot.
df = pd.read_csv("data.csv")
df.plot()
plt.show()

# Diagrama de Dispersion
# Se puede especificar que se dibuje un grafico de dispersion con el argumento kind.
df.plot(kind="scatter", x="Duration", y="Calories")
plt.show()

# Diagrama de dispersion donde no hay relacion entre las columnas.
df.plot(kind="scatter", x="Duration", y="Maxpulse")
plt.show()

# Histograma
# Se puede dibujar un histograma con el metodo plot() y especificando el argumento kind como histogram.
# Esto muestra la frecuencia de cada intervalo, en este caso cuanto duro cada entrenamiento.
df["Duration"].plot(kind="hist")
plt.show()
