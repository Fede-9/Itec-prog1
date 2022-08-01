# d = {'uno': 'primer', 1: 'segundo', ('q', 11): 'tupla!'} diccionario ridículo
# print(d[('q', 11)])

# diccionarios con pares homogéneos
capitales = {
    'England': 'London', 
    'France': 'Paris', 
    'Argentina': 'Buenos Aires', 
    'England': 'Essex'
}


print(capitales['France'])
#print(capitales[0]) # error, no existe la clave 0
capitales['Brazil'] = 'Brasilia' # agrega
capitales['France'] = 'Lille' # reemplaza

print(capitales)

edades = {'John': 31, 'Ryan': 11, 'Pam':22}
print(edades['Pam'])

ciudades = {'England': ['London', 'Liverpool', 'Manchester'], 'France': ['Paris', 'Lille', 'Marselle']}

print(ciudades['France'][0]) 