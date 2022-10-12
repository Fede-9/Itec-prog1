
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/avocado.csv')


atlanta = df[ df['region'] == 'Atlanta' ]

precio = atlanta['AveragePrice']
precioPromediado = precio.rolling(30).mean()
print(precio[:30])
print(precioPromediado[:30])

volumen = atlanta['Total Volume']

bolsasAguacate = atlanta['Total Bags']
sbolsas = atlanta['Small Bags']
lbolsas = atlanta['Large Bags']
xbolsas = atlanta['XLarge Bags']

# ordenes de los parametros: n° de filas, n° de columnas, el eje
plt.subplot(2,2,1)
plt.title('PRECIO AGUACATE')
plt.plot(precio, label='Precio', color='green')
plt.plot(precioPromediado, label='Precio Promediado', color='orange')
plt.legend()

plt.subplot(2,2,2)
plt.title('VOLUMEN DE AGUACATES')
plt.plot(volumen, label='Volumen Total', color='red')
plt.legend()

plt.subplot(2 ,2 ,3)
plt.title('BOLSAS TOTALES DE AGUACATES')
plt.plot(bolsasAguacate, label='Bolsas Totales', color='blue')
plt.legend()


plt.subplot(2,2,4)
plt.title('BOLSAS POR TAMAÑO')
plt.plot(sbolsas, label='Bolsas S', color='black')
plt.plot(lbolsas, label='Bolsas L', color='cyan')
plt.plot(xbolsas, label='Bolsas XL', color='yellow')
plt.legend()

plt.show()