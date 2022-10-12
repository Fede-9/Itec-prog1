# 5) Definir una clase que al ser instanciada reciba un valor numérico y cargue una lista de nombres 
# hasta esa cantidad.
#  Hacer también un método que muestre la lista completa.

class Listado():
    def __init__(self, cant):
        self.lista = []
        for x in range(cant):
            n = input('Nombre: ')
            self.lista.append(n)
        
    def getData(self):
        for e in self.lista:
            print(e)

# OTRA FORMA DE MOSTRAR LOS NOMBRES
    # def getData(self):
    #     nombres = []
    #     for e in self.lista:
    #         nombres.append(e)
    #     print(nombres)

if __name__ == "__main__":
    #cant = int(input("Ingrese un valor númerico: "))
    n = Listado(2)
    n.getData()



