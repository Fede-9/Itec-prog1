# METODOS

class Matematica():
    
    def suma(self):
        self.n1 = 5
        self.n2 = 2
        return self.n1 + self.n2
        

s = Matematica()
print(f'La suma es: {s.suma()}')


# otra forma
class Mat():
    def sumar(self, n1, n2):
        return n1 + n2

sumando = Mat()
print(sumando.sumar(2,2))



