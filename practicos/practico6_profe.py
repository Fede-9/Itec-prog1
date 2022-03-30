movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf", 
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf", 
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}

def getMovie(m, w):
    pP = m.find('(')
    nombre = m[:pP]
    anio = int(m[pP+1: pP+5])
    gene = m[pP+6:]
    if w == 'nombre':
        retorno = nombre
    elif w == 'año':
        retorno = anio
    elif w == 'genero':
        retorno = gene
    return retorno

#print(getMovie('Dumb & Dumber(1994)com', 'genero'))

def peliXgenero(genero):
    print('Películas de', genre[genero])
    for peli in movies:
        if getMovie(peli, 'genero') == genero:
            print('-', getMovie(peli, 'nombre'))

def peliXanio(anio):
    c = 0
    print('Películas anteriores a', anio, ':', end=' ')
    for peli in movies:
        if getMovie(peli, 'año') < anio:
            c += 1
    return c

def peliXletra(letra):
    letra = letra.upper()
    print('Películas cuyo nombre empieza con la letra', letra, ':')
    for peli in movies:
        if peli[0] == letra:
            salida = getMovie(peli, 'nombre') + '. Año: ' + str(getMovie(peli, 'año')) + '. Género: ' + genre[getMovie(peli, 'genero')]
            print(salida)

def menu():
    op = ''
    while op != '4':
        print('Menú de Opciones')
        print('1) Pelis x Género')
        print('2) Cantidad de películas estrenadas antes del año ...')
        print('3) Datos de las películas comenzadas con la letra ...')
        print('4) Salir')
        op = input('Ingrese opción: ')
        if op == '1':
            peliXgenero(input('Ingrese un género (act/sf/com): '))
        elif op == '2':
            print(peliXanio(int(input('Ingrese un año: '))))
        elif op == '3':
            peliXletra(input('Ingrese una letra: '))
        if op != '4':
            input('Enter para volver al menú')

menu()