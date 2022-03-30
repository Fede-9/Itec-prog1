# POLIMORFISMO CON HERENCIA 

class Ave():
    def volar(self):
        print('La mayoria de las aves pueden volar pero algunas no')

class Aguila(Ave):
    def volar(self):
        print('Las aguilas pueden volar !!')

class Gallina(Ave):
    def volar(self):
        print('La gallina NO puede volar !!')



objeto = Ave()
objeto.volar()
objAguila = Aguila()
objAguila.volar()
objGallina = Gallina()
objGallina.volar()
