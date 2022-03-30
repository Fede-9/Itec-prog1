class Animal():
    def dieta(self, i):
        self.dieta = ["omnívoro", "carnívoro", "herbívoro"]
        s = self.dieta[i]
        return s

    def setPeso(self, peso):
        self.peso = peso

    def getPeso(self):
        return self.peso

class Puma(Animal):
    def __init__(self,identificador, peso):
        self.setPeso(peso)

    def estadoAnimal(self):
        if self.getPeso() > 200:
            estado = "sano"
        else:
            estado = "enfermo"
        return estado

class Venado(Animal):
    def __init__(self,identificador,sexo, edad):
        self.i = identificador
        self.sexo = sexo
        self.edad = edad

class Jaula():
    def __init__(self, cant, animal):
        self.animal = animal
        print("Jaula de", animal)
        self.lista = []
        for i in range(cant):
            if animal == "puma":
                kg = int(input("Peso del puma: "))
                puma = Puma(i+1, kg)
                self.lista.append(puma)
            else:
                se = input("Sexo del venado: ")
                ed = int(input("Edad del venado: "))
                venado = Venado(i+1, se, ed)
                self.lista.append(venado)

    def mostrar(self):
        adultos = 0
        for x in self.lista:
            if self.animal == "puma":
                print(self.animal, x.dieta(1), x.getPeso(), x.estadoAnimal())
            else:
                print(self.animal, x.dieta(2), x.sexo, x.edad)
                if x.edad >=5 :
                    adultos += 1
        if self.animal == "venado":
            print(adultos)


j1 = Jaula(2, "puma")
j2 = Jaula(2, "venado")
j3 = Jaula(1, "puma")
j1.mostrar()
j2.mostrar()
j3.mostrar()
