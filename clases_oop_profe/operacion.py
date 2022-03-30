class Operacion: # clase abstracta, existe para ser heredada solamente, NO instanciada
    def tomar(self):
        self.n1 = int(input("Ingrese un numero: "))
        self.n2 = int(input("Ingrese otro numero: "))

    def operar(self): # método abstracto, no se ejecuta, para ser sobreescrito en las subclases
        self.resultado = None

    def mostrar(self):
        return self.resultado


class Suma(Operacion):
    def operar(self):
        self.resultado = int(self.n1) + int(self.n2)


class Resta(Operacion):
    def operar(self):
        self.resultado = int(self.n1) - int(self.n2)


if __name__ == "__main__":
    s = Suma()
    s.tomar()
    s.operar()
    print(s.mostrar())

    r = Resta()
    r.tomar()
    r.operar()
    print(r.mostrar())
    