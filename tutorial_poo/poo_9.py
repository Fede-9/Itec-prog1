# HERENCIA EJERCICIO PRACTICO

class Calculadora():
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresarDato(self):
        self.datos = [int(input('Ingresar dato '+str(i+1)+ ' = ')) for i in range(self.n)]

class Operaciones(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2) 

    def suma(self):
        a,b = self.datos
        s = a + b
        print(f'El resultado es: {s}')

    
    def resta(self):
        a,b = self.datos
        r = a - b
        print(f'El resultado es: {r}')

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def raizCuadrada(self):
        import math
        a, = self.datos
        print(f'El resultado es :{math.sqrt(a)}')


ejemplo = Operaciones()
print(ejemplo.ingresarDato())
print(ejemplo.suma())

ejemplo = Raiz()
print(ejemplo.ingresarDato())
print(ejemplo.raizCuadrada())