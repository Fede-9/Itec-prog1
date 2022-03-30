# 3) Usando las clases Operacion y Suma, definir otra que se llame Promedio y utilizarla.

from oper import Suma

class Promedio(Suma):
    def promedio(self):
        self.resu = self.resu / 2 

if __name__ == "__main__":
    p = Promedio()
    p.tomarDatos()
    p.opera()
    p.promedio()
    print(p.mostrarResultado())