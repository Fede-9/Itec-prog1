class Video():  # esta clase tiene los atributos comunes de las series y pelis. / el objetivo es unificar los atributos es como una clase abstracta.
    def __init__(self, nombre, visualizaciones, actores):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores

class Serie(Video):
    def __init__(self, nombre, visualizaciones, actores, temporadas): # temporadas es argumento propio de la clase Serie.
        Video.__init__(self, nombre, visualizaciones, actores)  # metodo super
        self.temporadas = temporadas

class Pelicula(Video):
    def __init__(self, nombre, visualizaciones, actores, duracion): # duracion es argumento propio de la clase Pelicula
        Video.__init__(self, nombre, visualizaciones, actores)  # metodo Super
        self.duracion = duracion

class Itecflix():
    def __init__(self):
        self.listaPelis = []
        self.listaSeries = []
        series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 5],
                    ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2]]

        pelis = [["Inception", 4760183, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
                    ["Batman Begins", 17319533, 'Christian Bale,Cillian Murphy,Michael Caine', 140],       
                    ["Inmortales", 35, 'Mirtha Legrand,Leonardo DiCaprio,Elizabeth The Second', 30]]

        for s in series:
            nombre, visu, actores, temporadas = s #asignacion multiple / es lo mismo que hacer s[0] s[1] s[2] s[3]
            serie = Serie(nombre, visu, actores.split(","), temporadas)
            self.listaSeries.append(serie)
            
        for p in pelis:
            nombre, visu, actores, duracion = p #asignacion multiple
            pelicula = Pelicula(nombre, visu, actores.split(","), duracion)
            self.listaPelis.append(pelicula)

    def masVisu(self):
        listaTotal = self.listaPelis + self.listaSeries
        mayorCantidadVisu = max([objeto.visualizaciones for objeto in listaTotal])
        for objeto in listaTotal:
            if objeto.visualizaciones == mayorCantidadVisu:
                return objeto.nombre

    def promedioDuracionPelis(self):
        total = 0
        for peli in self.listaPelis:
            total += peli.duracion
        return int(total / len(self.listaPelis))

    def actoresDeAmbas(self):
        def obtenerListaActores(listaVideos):
            listaDeListasDeActores = [video.actores for video in listaVideos] 
            listaPlanaDeActores = [actor for listaActores in listaDeListasDeActores for actor in listaActores] 
            # listaPlanaDeActores = []  # ES LO MISMO QUE LA LISTA POR COMPRENSION
            #         for listaActores in listaDeListasDeActores:
            #             for actor in listaActores:
            #                 listaPlanaDeActores.append(actor)
            return listaPlanaDeActores

        return [actor for actor in obtenerListaActores(self.listaSeries) if actor in obtenerListaActores(self.listaPelis)]

    def seriesMasDe3Temporadas(self):
        return [serie.nombre for serie in self.listaSeries  if serie.temporadas > 3]
        
plataforma = Itecflix()

print(f"El video mas visto: {plataforma.masVisu()}")

print(f"Promedio de duración de las películas: {plataforma.promedioDuracionPelis()} minutos")

print("Actores que trabajan en series y películas:", end=" ")
for actor in plataforma.actoresDeAmbas():
    print(f"- {actor} ", end=" ")
print()

print("Series que tienen más de 3 temporadas:", end=" ")
for serie in plataforma.seriesMasDe3Temporadas(): 
    print(f"- {serie}", end="")
print()