class Puerta():
    def __init__(self, puerta, ubicacion):
        self.puerta = puerta
        self.ubicacion = ubicacion

    def abrir(self):
        print(f'Abriendo la puerta {self.puerta} {self.ubicacion}')

    def cerrar(self):
        print(f'Cerrando la puerta {self.puerta} {self.ubicacion}')


class Auto():
    def __init__(self):
        self.p1 = Puerta('delantera','izquierda')
        self.p2 = Puerta('delantera','derecha')
        self.p3 = Puerta('trasera','izquierda')
        self.p4 = Puerta('trasera','derecha')



auto = Auto()
auto.p1.abrir()
auto.p3.cerrar()

