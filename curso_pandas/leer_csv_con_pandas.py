import pandas as pd

df = pd.read_csv('./data/avocado.csv')
# asi comienza desde el cero
df = pd.read_csv('./data/avocado.csv', index_col=0)
# asi comienza desde las fechas
df = pd.read_csv('./data/avocado.csv', index_col=['Date'])
# para que me muestre el encabezado y las 3 primeras filas
print(df.head(3))

