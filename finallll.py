class Puerta():
    def __init__(self, puerta, ubicacion):
        self.puerta = puerta
        self.ubicacion = ubicacion

    def abrirPuerta(self):
        print("Abierta la puerta", self.puerta, self.ubicacion)

    def cerrarPuerta(self):
        print("Cerrada la puerta", self.puerta, self.ubicacion)




class Auto():
    def __init__(self):
        self.p1 = Puerta("delantera", "derecha")
        self.p2 = Puerta("delantera", "izquierda")
        self.p3 = Puerta("trasera", "derecha")
        self.p4 = Puerta("trasera", "izquierda")
      


auto1 = Auto()
auto1.p1.abrirPuerta()
auto1.p3.cerrarPuerta()


# OTRA FORMA PARA HACERLO

class Puerta():
    def __init__(self, puerta, ubicacion):
        self.puerta = puerta
        self.ubicacion = ubicacion


class Auto(Puerta):

    def abrirPuerta(self):
        print(f'Abriendo la puerta: {self.puerta} {self.ubicacion}')

    def  cerrarPuerta(self):
        print(f'Cerrando puerta: {self.puerta} {self.ubicacion}')


auto1 = Auto('delantera','izquierda')
auto1.abrirPuerta()



# OTRA FORMAAA

class Puerta():
        def __init__(self,puerta,ubicacion):
            self.puerta = puerta
            self.ubicacion = ubicacion
    
        def abrirPuerta(self):
            print(f'Abrienda puerta: {self.puerta} {self.ubicacion}')

        def  cerrarPuerta(self):
            print(f'Cerrando puerta: {self.puerta} {self.ubicacion}')
        

puerta1 = Puerta('derecha','delantera')
puerta1.abrirPuerta()



# POLIMORFISMO

class Dogo():
    def hablar(self):
        print('soy un dogo')


class Caniche():
    def hablar(self):
        print('soy un caniche')


def hablando(objeto):
    objeto.hablar()



perro1 = Dogo()
perro2 = Caniche()


hablando(perro1)
hablando(perro2)


# perro1.hablar()
# perro2.hablar()



#Polomorfismo 

class Perro(): #Clase Padre
    def hablar(self): #Método Hablar
        print ("Soy el perro padre...")

class Caniche(Perro): #Clase Hija
    def hablar (self): #Método Hablar
        print ("Soy un caniche ...")
        

class Dogo(Perro): #Clase Hija
    def hablar (self, mensaje): #Método Hablar
        print (mensaje)

perro = Perro() #instancia
caniche = Caniche() #Instancia
dogo = Dogo() #Instancia

perro.hablar()#llamamos al metodo
caniche.hablar() #Llamamos al método
dogo.hablar("Soy una dogo, este es mi mensaje") #Llamamos al método