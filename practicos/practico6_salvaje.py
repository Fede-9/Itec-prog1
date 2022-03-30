# Dados los datos anteriores, obtener tres resultados de salida por pantalla.

# 1-Nombres de las películas según un género solicitado.
# 2-La cantidad de películas estrenadas antes de un año solicitado.
# 3-Nombres, años de estreno y géneros de las películas cuyo nombre comienza con una letra pedida al usuario.

movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
 "Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
 "Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}

g = input('Qué género desea buscar?: ')
a = int(input('Ingrese un año: '))
c = 0
l = input('Ingrese letra: ')
pelisXgenero = []
pelisXletra = []
for peli in movies:
    posiParent = peli.find('(')
    nombre = peli[:posiParent]
    anio = int(peli[posiParent+1:posiParent+5])
    genero = peli[posiParent+6:]
    #print(nombre, anio, genero)
    if genero == g:
        pelisXgenero.append(nombre)
    if anio < a:
        c += 1
    if nombre[0] == l:
        dato = nombre + ". Año: " + str(anio) + ". Género: " + genre[genero]
        pelisXletra.append(dato)


print('Películas del género', genre[g])
for e in pelisXgenero:
    print('-', e)
print('Cantidad de pelis anteriores al', a, ":", c)
print('Películas que comienzan con la letra', l)
for e in pelisXletra:
    print('-', e)

