import pandas as pd

personas = {
    'nombre': ['Federico','Lucas','Juan'],
    'edad': [24, 22, 18],
    'pais': ['Argentina','España','Mexixo']
}

df = pd.DataFrame(personas)
print(df)