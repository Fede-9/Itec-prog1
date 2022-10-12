from cProfile import label
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



df = pd.read_csv('./data/avocado.csv')
# print(df.head(5))

chicago = df[df['region'] == 'Chicago']
# print(chicago.head(10))



# aca le digo que en vez de usar el indice 0,1,2,3,etc  use a la fecha como indice
chicago = chicago.set_index('Date')
# para ordenar las fechas
chicago = chicago.sort_values(by='Date')
# print(chicago.head(10))




# GRAFICO CON MATPLOTLIB

# determino cuantos datos quiero graficar
MAX_SAMPLES = 100


precio = chicago['AveragePrice'][:MAX_SAMPLES]
cantidad = chicago['Total Volume'][:MAX_SAMPLES]

plt.plot(precio, label='Precio Medio')
plt.plot(cantidad, label='Volumen total')

plt.title('Precio de los aguacates vs tiempo')
plt.xlabel('Fecha')
plt.xticks(rotation=90)
plt.ylabel('Precio en $')
plt.legend()

plt.show()
