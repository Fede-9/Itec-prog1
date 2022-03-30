# 2) Desarrolla una clase Cafetera con atributos capacidadMaxima (la cantidad máxima de café que puede contener la cafetera) y cantidadActual 
# (la cantidad actual de café que hay en la cafetera). Implementa, al menos, los siguientes métodos: 
# Constructor: establece la capacidad máxima en 1000 (c.c.)  y la actual en cero (cafetera vacía). 
# llenarCafetera(), servirTaza(int): simula la acción de servir una taza con la capacidad indicada, si la cantidad actual 
# de café no alcanza para llenar la taza, se sirve lo que quede. 
# vaciarCafetera(): pone la cantidad de café actual en cero.  
# mostrarCafetera(): nos dice cuanto café hay.

class Cafetera():
    def __init__(self):
        self.capacidadMaxima = 1000
        self.cantidadActual = 0

    def llenarCafetera(self): #simula la acción de servir una taza con la capacidad indicada
        self.cantidadActual = self.capacidadMaxima

    def servirTaza(self, cantidad):
        if self.cantidadActual > cantidad:
            self.cantidadActual -= cantidad
        else:
            print(f'No quedo tanta cantidad, se lleno la taza con {self.cantidadActual} ml de cafe')
            self.vaciarCafetera()

    def vaciarCafetera(self): #pone la cantidad de café actual en cero.
        self.cantidadActual = 0        
    
    def mostrarCafetera(self): #nos dice cuanto café hay.
        return f'Cantidad de cafe disponible: {self.cantidadActual} ml'


if __name__ == '__main__':
    cafetera1 = Cafetera()
    print(cafetera1.mostrarCafetera())
    cafetera1.llenarCafetera()
    print(cafetera1.mostrarCafetera())
    cafetera1.servirTaza(300)
    print(cafetera1.mostrarCafetera())
    cafetera1.servirTaza(800)
    print(cafetera1.mostrarCafetera())
    