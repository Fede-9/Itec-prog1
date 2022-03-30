movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}

def construirListas(lista):
    peligenero = []
    peliaño=[]
    pelinombre=[]
    for peli in lista:
        posiciongenero = peli.find(')')
        genero = peli[posiciongenero+1:]
        peligenero.append(genero)
        posicionaño=peli.find('(')
        año=peli[posicionaño+1:posiciongenero]
        peliaño.append(año)
        nombre=peli[:posicionaño]
        pelinombre.append(nombre)
    return peligenero, peliaño, pelinombre

generos, años, nombres = construirListas(movies)

def todogeneros(gen):
    for i in range(len(nombres)):
        if gen==generos[i]:
            print("-",end=""),print(nombres[i])
todogeneros("sf")

def añoestreno(año):
    suma=0
    for i in range(len(años)):
        if int(año)>=int(años[i]):
            suma+=1
    print("Cantidad de peliculas estrenadas antes del año",año,"es",suma)
añoestreno("2000")

def nombreañogenero(inicial):
     iniciales=[]
     for i in range(len(nombres)): 
         if inicial==nombres[i][0]:
             respuesta = nombres[i]+'. '+ "Año: " + años[i] +'. ' + "Genero: "+ genre[generos[i]]
             iniciales.append(respuesta)
     return iniciales

for e in nombreañogenero("T"):
    print(e)
