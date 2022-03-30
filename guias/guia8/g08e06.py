# 6) Crear una aplicación para gestionar un videoclub.
# Todos los productos tienen:
# Titulo, precio alquiler, plazo(dias), alquilado (si/no)
# Genero (accion, fantasía, etc), año, director, protagonista
# Se mantiene un listado de clientes:
# – Nº cliente, nombre, dirección, teléfono, productos alquilados
# Se guarda un listado de registros de alquiler:
# – Cliente, producto, fecha alquiler, fecha devolucion, importe
# Crear una aplicación de consola con el siguiente menú:
# – Lista productos
# – Añadir producto
# – Ficha producto
# – Lista clientes
# – Añadir cliente
# – Ficha cliente
# – Alquiler producto

from os import system
from validacion_entero import validacionEntero



def seguirPrograma():
    sigue = input('Ingrese cualquier tecla para continuar, "Q" para finalizar: ')
    if sigue.lower() == 'q':
        return False  
    else:
        return True


class Pelicula():
    def __init__(self, titulo, precioAlquiler,genero, anio, director, protagonista):
        self.titulo = titulo
        self.precioAlquiler = precioAlquiler
        self.diasAlquiler = 0
        self.alquilado = False
        self.genero = genero
        self.anio = anio
        self.director = director
        self.protagonista = protagonista
        
    
    def setDiasAlquiler(self, diasAlquiler):
        """ Establece los dias de alquiler de la pelicula"""
        self.diasAlquiler = diasAlquiler
        self.alquilado = True
    
    
    
    def getAlquilado(self):
        """ Chequea si la pelicula esta alquilada o no"""
        return self.alquilado
    
    def getMovie(self):
        print(f'Nombre: {self.titulo}')
        print(f'Genero: {self.genero}')
        print(f'Director: {self.director}')
        print(f'Protagonista: {self.protagonista}')
        print(f'Año: {self.anio}')
        print(f'Costo alquiler: {self.precioAlquiler}')
        if self.getAlquilado():
            print(f'Pelicula ya alquilada, dias restantes de alquiler {self.diasAlquiler}')
        print('\n')
        
    def getMovieName(self):
        return self.titulo
    


class Cliente():
    def __init__(self,nombre:str, direccion:str, telefono: int):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.alquiladas = []
        pass

    def setMovie(self, movie:Pelicula):
        if type(movie) == Pelicula:
            self.alquiladas.append(movie)
        else:
            print('No se agrego la pelicula, no es del tipo pelicula.')
        pass
    
    def getCliente(self):
        print(f'Nombre: {self.nombre} ')
        print(f'Direccion: {self.direccion} ')
        print(f'Telefono: {self.telefono} ')
        if len(self.alquiladas) >= 1:
            print('\nPeliculas alquiladas: ')
            for p in self.alquiladas:
                p.getMovie()
        print('\n')
    
    def getClienteName(self):
        return self.nombre

    

class Videoclub():
    def __init__(self):
        """ Clientes agg a lo bruto para testeo."""
        self.clientes = [Cliente('Cliente0', 'Direccion', 12345),
        Cliente('Cliente1', 'Direccion1', 12345),
        Cliente('Cliente2', 'Direccion2', 12345),
        Cliente('Cliente3', 'Direccion3', 12345)]
        self.peliculas = [Pelicula('Pelicula0',200,'Genero',1999,'Director','Protagonista'),
        Pelicula('Pelicula1',200,'Genero1',1999,'Director1','Protagonista1'),
        Pelicula('Pelicula2',200,'Genero2',1999,'Director2','Protagonista2'),
        Pelicula('Pelicula3',200,'Genero3',1999,'Director3','Protagonista3')]
    
    # Metodos peliculas
    def printMovies(self):
        """ Printea todas las peliculas disponibles"""
        if len(self.peliculas) >= 1: 
            for i in range(len(self.peliculas)):
                print(f'Pelicula {i}')
                self.peliculas[i].getMovie()
        else:
            print('No existen peliculas para mostrar')
    
    def addMovies(self):
        """ Agrega una pelicula a la lista de peliculas"""
        titulosPeliculas = list(map(lambda x: x.getMovieName().lower(),self.peliculas))
        tituloAux = input('Ingrese el titulo de la pelicula: ')
        if tituloAux.lower() not in titulosPeliculas:
            precioAux = validacionEntero('Precio alquiler de la pelicula: ')
            generoAux = input('Ingrese el genero de la pelicula: ')
            anioAux = validacionEntero('Anio de la pelicula: ')
            directorAux = input('Director de la pelicula: ')
            protagonistaAux = input('Protagonista de la pelicula: ')
            self.peliculas.append(Pelicula(tituloAux, precioAux, generoAux, anioAux, directorAux, protagonistaAux))
        else:
            print('La pelicula ya existe, no se agrego')
    

    def printMoviesName(self):
        titulosPeliculas = list(map(lambda x: x.getMovieName().lower(),self.peliculas))
        if len(titulosPeliculas) >= 1:
            print('Peliculas disponibles: ')
            for i in range(len(titulosPeliculas)):
                print(f'{i} - {titulosPeliculas[i].title()}')
        else:
            print('No existen peliculas para mostrar')
    
    def chooseMovie(self):
        numPeli = validacionEntero('Ingrese numero correspondiente a la pelicula: ')
        """" Retorna la pelicula correspondiente en la lista."""
        try:
            return self.peliculas[numPeli]
        except:
            return f'No existe la pelicula'
        
    def deleteMovie(self):
        numPeli = validacionEntero('Ingrese numero correspondiente a la pelicula: ')
        try:
            if self.peliculas[numPeli]:
                self.peliculas.remove(self.peliculas[numPeli])
        except:
            print('No existe la pelicula o ya fue eliminada.')


    
   # Metodos clientes  
    def printClients(self):
        if len(self.clientes) >= 1:
            """ Printea los clientes"""
            for i in range(len(self.clientes)):
                print(f'Cliente {i}')
                self.clientes[i].getCliente()
        else:
            print('No existen clientes para mostrar')

    def addClient(self):
        """ Agrega cliente  """
        nombresClientes = list(map(lambda x: x.getClienteName().lower(), self.clientes))
        nombreAux = input('Ingrese el nombre de cliente: ')
        if nombreAux.lower() in nombresClientes:
            print('El nombre ya existe, no se agrego el cliente')
        else:
            direccionAux = input('Ingrese la direccion del cliente: ')
            telefonoAux = validacionEntero('Telefono: ')
            self.clientes.append(Cliente(nombreAux,direccionAux, telefonoAux))
    
    def printClientsNames(self):
        nombresClientes = list(map(lambda x: x.getClienteName().lower(), self.clientes))
        for i in range(len(nombresClientes)):
            print(f'{i} - {nombresClientes[i].title()}')
    
    def chooseClient(self):
        numClient = validacionEntero('Ingrese el numero de cliente: ')
        try:
            if self.clientes[numClient]:
                return self.clientes[numClient]
        except:
            return f'No existe el cliente'

    def deleteClient(self):
        numClient = validacionEntero('Ingrese el numero de cliente: ')
        try:
            if self.clientes[numClient]:
                self.clientes.remove(self.clientes[numClient])
        except:
            print('No existe el cliente o ya fue eliminado')



    def rentMovie(self):
        print('Peliculas disponibles: ')
        self.printMovies()
        pelicula = self.chooseMovie()
        if type(pelicula) == Pelicula and (not pelicula.getAlquilado()):
            system('cls')
            self.printClientsNames()
            cliente = self.chooseClient()
            if type(cliente) == Cliente:
                dAlquiler = validacionEntero('Dias de alquiler de la pelicula: ')
                pelicula.setDiasAlquiler(dAlquiler)
                cliente.setMovie(pelicula)
            else:
                print(cliente)
        else:
            print('No se pudo agregar la pelicula, ya está alquilada o no existe')

        
    def menu(self):
        menu = {}
        sigue = True

        menu['1'] = 'Lista peliculas'
        menu['2'] = 'Añadir pelicula'
        menu['3'] = 'Ficha producto'
        menu['4'] = 'Lista clientes'
        menu['5'] = 'Añadir cliente'
        menu['6'] = 'Ficha cliente'
        menu['7'] = 'Alquiler producto'
        menu['8'] = 'Eliminar producto'
        menu['9'] = 'Eliminar cliente'
        menu['10'] = 'Salir'
        while sigue:
            system('cls')
            for k,v in menu.items():
                print(f'{k} - {v}')
            opcion = validacionEntero('Ingrese una opcion: ')
            if opcion == 1:
                system('cls')
                self.printMovies()
                sigue = seguirPrograma()
            elif opcion == 2:
                system('cls')
                self.addMovies()
                sigue = seguirPrograma()
            elif opcion == 3:
                system('cls')
                self.printMoviesName()
                peliElegida = self.chooseMovie()
                if type(peliElegida) == Pelicula:
                    system('cls')
                    peliElegida.getMovie()
                else:
                    system('cls')
                    print(peliElegida)
                sigue = seguirPrograma()
            elif opcion == 4:
                system('cls')
                self.printClients()
                sigue = seguirPrograma()
            elif opcion == 5:
                system('cls')
                self.addClient()
                sigue = seguirPrograma()
            elif opcion == 6:
                system('cls')
                self.printClientsNames()
                clienteElegido = self.chooseClient()
                if type(clienteElegido) == Cliente:
                    clienteElegido.getCliente()
                else:
                    print(clienteElegido)
                sigue = seguirPrograma()
            elif opcion == 7:
                self.rentMovie()
                sigue = seguirPrograma()
            elif opcion == 8:
                self.printMoviesName()
                self.deleteMovie()
                sigue = seguirPrograma()
                pass
            elif opcion == 9:
                self.printClientsNames()
                self.deleteClient()
                sigue = seguirPrograma()
                pass
            elif opcion == 10:
                sigue = False   
                



if __name__ == '__main__':
    videoclub = Videoclub() 
    videoclub.menu()
    print('Salio del menu')

    
    