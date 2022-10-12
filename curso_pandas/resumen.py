from random import random
import pandas as pd

df = pd.read_csv('./data/avocado.csv')

# para ver las filas que quiero con sus encabezados
print(df.head())
# para calcular la media, desviacion, porcentajes,etc
print(df.describe())
# para eliminar datos NaN
print(df.dropna())
# para llenar los espacios NaN
print(df.fillna(0))
# para rellenar en determinados lugares
print(df.fillna({'lugar1': 0, 'lugar2': 1 }))
# para traer determinada columna
print(df['Date'])
# para traer mas de una columna
print(df[['Date', 'AveragePrice']])
# filtrado de filas
# primer manera
print(df.iloc[0])
print(df.iloc[0:3])
# segunda manera
print(df.iloc[0,1,2])
# filtado de filas y columnas
print(df.iloc[0:3], ['Date','AveragePrice'])
# filtrado por condicion
print(df[df['Small Bags'] > 100])
print(df[(df['Small Bags'] > 100) & (df['Large Bags'] > 20)])
# para buscar donde contenga determinada palabra
print(df[df['Nombre de la columna'].str.contains('palabra que quiero buscar')])
# crear nuevas columnas
def calcularGanancias(parametro):
    ganancia = parametro * random.randint(3,5)
    return ganancia

df['nombre de la nueva columna'] = df['elijo la funcion que le quiero aplicar la funcion'].apply(calcularGanancias())