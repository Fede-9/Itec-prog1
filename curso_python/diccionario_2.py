# Indexacion y modificacion de diccionario

diccionario = {'pais':'argentina' , 'habitantes':500}

print(diccionario['pais'])
print(diccionario['habitantes'])

# Get
print('------------- GET ---------------')
print(diccionario.get('pais'))     # PARA OBTENER LOS VALORES
print(diccionario.get('habitantes'))

# Update
print('------------- UPDATE ---------------')
diccionario.update( {'pais':'brasil'} )
print(diccionario)
diccionario.update( {'Color':'Azul'} )   #como no existe la clave la agrega al diccionario.
print(diccionario)

# Copy
print('------------- COPY ---------------')
copia_diccionario = diccionario.copy()
print(copia_diccionario)

# Otra forma de modificar un diccionario
print('---------------------------')
diccionario['pais'] = 'Italia' # diccionario.update( {'pais':'Italia'} )
print(diccionario)

# Clear
print('------------- CLEAR ---------------')
diccionario.clear()
print(diccionario)
print(type(diccionario))

print('---------------------------')
numero = 5
print(numero)
del numero      #me tira error porque el 'del' elimina la variable, en cualquier tipo de estructura
print(numero)