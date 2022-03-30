# 2) Definir una clase Auto con un método que le permita poner la marca y el año. 
# En el programa principal declarar tres instancias (objetos), cargarlas y mostrar las marcas 
# de los tres autos.

class Auto():
    def __init__(self,marca,año):
        self.marca = marca
        self.año = año

    def setMarca(self,otraMarca):
        self.otraMarca = otraMarca

        return self.otraMarca

a1 = Auto('ford',1998)
a2 = Auto('chevrolet',2000)
a3 = Auto('mustan',1986)

print(a1.marca)
print(a2.marca)
print(a3.marca)

for auto in a1,a2,a3:
    print(auto.marca)

print(a1.setMarca('fiat'))  #para colocar otra marca