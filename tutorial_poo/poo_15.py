# METODO SUPER

class Mamifero():
    def __init__(self,nombre):
        print(nombre,'Es un animal de sangre caliente')

class Leon(Mamifero):
    def __init__(self):
        print('El leon es un animal de cuatro patas')
        super().__init__('Zimba')

nuevoLeon = Leon()
