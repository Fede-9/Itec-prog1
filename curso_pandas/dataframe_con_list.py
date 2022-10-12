import pandas as pd

# PRIMER METODO

colums = ['Marca', 'Precio', 'Disponibilidad']
cocheA = ['Mercedes', 150000, True]
cocheB = ['BMW', 200000, False]


df = pd.DataFrame([cocheA, cocheB], columns=colums)

# print(df)



# SEGUNDO METODO


marcas = ['Audi','Mercedes','BMW','Mercedes']
precio = [1000, 454, 12234, 98999]
disponibilidad = [True, True, False, True]


df = pd.DataFrame(
    list(zip(marcas,precio,disponibilidad)),
    columns=['Marca', 'Precio', 'Disponibilidad']
)

# print(list(zip(marcas,precio,disponibilidad)))

# print(df)





# TERCER METODO


marcas = ['Audi','Mercedes','BMW','Mercedes']
precio = [1000, 454, 12234, 98999]
disponibilidad = [True, True, False, True]

diccionario = {
    'marcas': marcas,
    'precios': precio,
    'disponibilidad': disponibilidad
}

df = pd.DataFrame(diccionario)
print(df)