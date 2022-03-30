# POLIMORFISMO

class Animales():
    def __init__(self,nombre):
        self.nombre = nombre

    def tipoAnimal(self):
        pass

class Leon(Animales): #leon es clase hija de animales
    def tipoAnimal(self):
        print('animal salvaje')

class Perro(Animales):
    def tipoAnimal(self):
        print('animal domestico')


nuevoAnimal = Leon('Zimba')
nuevoAnimal.tipoAnimal()

otroAnimal = Perro('Roko')
otroAnimal.tipoAnimal()