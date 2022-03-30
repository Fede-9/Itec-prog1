# Tenemos un archivo de entrada pelis.json con datos de películas obtenido de http://www.omdbapi.com/
# y lo recorreremos para obtener los siguientes datos:
# Nombre
# Actor o actriz principal
# Rating de Rotten Tomatoes
# Recaudación


# Esos datos serán grabados en un nuevo archivo, llamado pelis.csv, cuya estructura será la siguiente:

# Nombre, Actor, Rating, Recaudación
# Peli-1,Actor-1,78,123456789
# Peli-2,Actriz-1,91,987654321
# ...



# Realizar dos soluciones:


# 1) Sin usar ninguna biblioteca externa (ningún import).

# 2) Usando la biblioteca json


# ACTIVIDAD 1 : leer y crear nuevo.


peli = open('pelis.json', 'r')
lectura = peli.read()
lectura = eval(lectura) # convierte de str a dict
peli.close()


nueva_peli = open('pelis.csv', 'w')
nueva_peli.write('Nombre, Actor, Rating, Recaudacion\n')
for clave in lectura:
    nombre = clave['Title']
    actor = clave['Actors']
    rating = clave['Ratings']
    recaudacion = clave['BoxOffice']
    recaudacionSinComa = recaudacion.replace(',','')  # Le quito las comas de los numeros 
    
    for valor in rating:
        if valor['Source'] == 'Rotten Tomatoes':
            ratingRt = valor['Value']
            nueva_peli.write(nombre + ', ' + actor[:actor.find(',')] + ', ' + ratingRt[:-1] + ', ' + recaudacionSinComa[1:] + '\n')
    
nueva_peli.close()
    

# Luego de ello, con otro programa (o bien el mismo con otra función en el menú) se leerá pelis.csv y se mostrará por
#  pantalla el Rating promedio y la suma de las recaudaciones de todas las películas.


pelicula = open('pelis.csv', 'r')
lectura = pelicula.readlines()
lectura.pop(0)
pelicula.close()


contPelis = 0
sumaRating = 0
sumaRecaudacion = 0
for i in lectura:
    listaPelis = i.split(',')
    ratinngPeli = listaPelis[2]
    recaudacionPeli = listaPelis[3]
    contPelis += 1
    sumaRating += int(ratinngPeli)
    sumaRecaudacion += int(recaudacionPeli)
    

print('Rating promedio: %',sumaRating/contPelis)
print('Suma de las recaudaciones: $',sumaRecaudacion)
    
    
