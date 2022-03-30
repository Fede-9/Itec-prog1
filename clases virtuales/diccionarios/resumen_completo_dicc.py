# Diccionarios: son estructuras de datos que nos permiten almacenar distintos valores.
# Los datos se almacenan asociados a una clave unica, tenemos una relacion clave:valor


miDiccionario = {'España':'Madrid','Peru':'Lima','Alemania':'Berlin'}
print(miDiccionario['Peru']) #accedemos a su valor
print(miDiccionario)

miDiccionario['Venezuela'] = 'Caracas' #agregamos ala diccionario
print(miDiccionario)

miDiccionario['España'] = 'Barcelona' #modifico el valor si la clave ya existe.
print(miDiccionario)

del miDiccionario['España']  #elimino la clave y el valor.
print(miDiccionario)

# Diccionario con distintos elementos
dic2 = {'Cometto':'Federico',25:True,'Sueldo':4000}
print(dic2[25])


# Diccionario con tuplas

llaves = ('España','Francia','Inglaterra')
dicPaises = {llaves[0]:'Madrid',llaves[1]:'Paris',llaves[2]:'Londres'}
print(dicPaises)


datosPersonales = {'Apellido':'Garcia','Años':{2010,2020,2003,2004}}
print(datosPersonales)
print(datosPersonales['Años'])


datosPersonales = {'Apellido':'Garcia','Años':{1:2010,2:2020,3:2003,4:2004}}
print(datosPersonales)
print(datosPersonales['Años'])

print(datosPersonales.get('Apellido','Saby')) # si no exite la clave 'Apellido' me devuelve Saby
print(datosPersonales.get('Apell','Saby')) # si no exite la clave 'Apellido' me devuelve Saby


print(datosPersonales.keys())  # me devuelve los las claves
print(datosPersonales.values()) # me devuelve los valores
print(list(datosPersonales.values())) # los convierto en lista