# POLIMORFISMO POR FUNCION

class Tomate():
    def tipo(self):
        print('es un vegetal')

    def color(self):
        print('rojo')

class Manzana():
    def tipo(self):
        print('es una fruta')

    def color(self):
        print('verde')

def funcion(objeto):
    objeto.tipo()
    objeto.color()



nuevoTomate = Tomate()
funcion(nuevoTomate)
nuevaManzana = Manzana()
funcion(nuevaManzana)