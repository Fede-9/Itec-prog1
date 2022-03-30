class Operacion():
    def tomarDatos(self):
        self.n1 = int(input('Primer número: '))
        self.n2 = int(input('Segundo número: '))
    
    def opera(self):
        self.resu = None
        
    def mostrarResultado(self):
        return self.resu

class Suma(Operacion):
    def opera(self):
        self.resu = self.n1 + self.n2


class Resta(Operacion):
    def opera(self):
        self.resu = self.n1 - self.n2
        

if __name__ == '__main__':
    s = Suma()
    s.tomarDatos()
    s.opera()
    print(f'Resultado de la operacion: {s.resu}')
    r = Resta()
    r.tomarDatos()
    r.opera()
    print(f'Resultado de la operacion: {r.resu}')