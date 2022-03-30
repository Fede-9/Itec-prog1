# Dados los datos anteriores, obtener tres resultados de salida por pantalla.

# 1-Nombres de las películas según un género solicitado.
# 2-La cantidad de películas estrenadas antes de un año solicitado.
# 3-Nombres, años de estreno y géneros de las películas cuyo nombre comienza con una letra pedida al usuario.





movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}

act1=genre['act']
sf1=genre['sf']
com1=genre['com']

nombrePelicula=[]
añoPelicula=[]
generoPelicula=[]
inicialPelicula=[]

for i in range(len(movies)):
    posParentesis1=movies[i].find('(')
    posParentesis2=movies[i].find(')')
    año=movies[i][posParentesis1+1:posParentesis2]
    añoPelicula.append(año)
    nombre=movies[i][:posParentesis1]
    nombrePelicula.append(nombre)
    genero=movies[i][posParentesis2+1:]
    generoPelicula.append(genero)
    
#ACTIVIDAD Nº1   
def buscarPeli(usuario):
    eleccion=[]
    if usuario=='act':
        print(f'Ustes seleciono el genero: {act1} ')
    elif usuario=='sf':
        print(f'Usted selecciono el genero: {sf1}')
    elif usuario=='com':
        print(f'Usted selecciono el genero: {com1}')
    for x in range(len(generoPelicula)):
        if usuario==generoPelicula[x]:
            eleccion.append(nombrePelicula[x]) 
    return eleccion   
    

print('----- GENEROS DE PELICULAS ---------\n',
genre)
usuario1 = input('Ingrese genero de la pelicula que desea (act/sf/com): ')
peliSelecc=buscarPeli(usuario1)
print(f'Peliculas disponibles segun genero seleccionado:\n',peliSelecc)



#ACTIVIDAD Nº2

def buscarAño(estreno):
    cont=0
    for w in range(len(añoPelicula)):
        if estreno>int(añoPelicula[w]):
            cont+=1  
    return cont  

usuario2 = int(input('Escriba el año de estreno de la pelicula: '))
estrenoSelecc=buscarAño(usuario2)
print(f'Cantidad de peliculas antes del año {usuario2}: ',estrenoSelecc)




#ACTIVIDAD 3

def peliCompleta(todo):
    salidapelicula=[]
    for z in range(len(nombrePelicula)): 
        if str(todo.upper())==nombrePelicula[z][0]:
            salidapelicula.append(movies[z])
        
    return salidapelicula


usuario3=input('ingrese letra de la pelicula que desea: ')
nombreSelecc=peliCompleta(usuario3)
print('Peliculas: ',nombreSelecc)