# La función incorporada super() permite invocar un método o atributos de una clase padre desde una clase hija.

# en este ejemplo invocamos al metodo

class ClassA:
    def message(self):
        print("Hola",end=' ')

class ClassB(ClassA):
    def message(self):
        super().message()
        print("mundo!")

b = ClassB()
b.message()