class Puerta():
    def __init__(self,puerta,ubicacion):
        self.puerta = puerta
        self.ubicacion = ubicacion

    def abrir(self):
        print(f'Abriendo la puerta {self.puerta} {self.ubicacion}')

    def cerrar(self):
        print(f'Cerrando la puerta {self.puerta} {self.ubicacion}')


class Auto(Puerta):
    def __init__(self, puerta, ubicacion,tipoAuto):
        super().__init__(puerta, ubicacion)
        self.tipoAuto = tipoAuto


auto = Auto('delantera','derecha','Ford')
auto.abrir()
print(auto.tipoAuto)


