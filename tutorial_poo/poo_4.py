# METODO CONSTRUCTOR

class Ropa():
    def __init__(self):
        self.marca = 'nike'
        self.talla = 'L'
        self.color = 'rojo'

    def getDatos(self):
        return f'{self.marca}\n {self.talla}\n {self.color}'

camisa = Ropa()
print(camisa.marca)
print(camisa.talla)
print(camisa.color)
print(camisa.getDatos())

########################################################################
print(' --------------------------------------------------------------- ')

class Calculadora():
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(2,3)
print(operacion.suma)
print(operacion.resta)
print(operacion.producto)
print(operacion.division)