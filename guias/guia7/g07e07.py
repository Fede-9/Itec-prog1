# 7) Agregar al ejercicio 2 (clase Auto) un método que obtenga la antigüedad. 
# En el programa principal mostrar cuáles autos tienen más de 5 años.

from datetime import datetime

class Auto():
    def __init__(self, marca, año):
        self.marca = marca
        self.anio = año

    def obtenerAntig(self):
        return datetime.now().year - self.anio

listaAutos = []
a1 = Auto('Ford', 1990)
a2 = Auto('Nissan', 2018)
a3 = Auto('Chevy', 2001)

listaAutos.append(a1)
listaAutos.append(a2)
listaAutos.append(a3)


for auto in listaAutos:
    if auto.obtenerAntig() >= 5:
        print(auto.marca)