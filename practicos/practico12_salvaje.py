class Animal():
    def esSano(self, animal, peso):
        if (animal == "puma" and peso > 200) or (animal == "venado" and peso > 120):
            return "sano"
        else:
            return "enfermo"


class Puma(Animal):
    def __init__(self, identificador, edad, peso):
        self.identificador = identificador
        self.edad = edad
        self.peso = peso

    def esAdulto(self):
        if self.edad >= 5:
            return True
        else:
            return False


class Venado(Animal):
    def __init__(self, identificador, peso):
        self.identificador = identificador
        self.peso = peso


class Jaula():
    def __init__(self, animal, cantidad):
        self.animal = animal
        self.jaula = []
        for x in range(cantidad):
            peso = int(input(f"Ingrese el peso del {animal}: "))
            if animal == "puma":
                edad = int(input(f"Ingrese la edad del {animal}: "))
                ani = Puma(x + 1, edad, peso)
            else:
                ani = Venado(x + 1, peso)
            self.jaula.append(ani)

    def mostrarJaula(self):
        for ani in self.jaula:
            print(f"{ani.identificador} - {ani.esSano(self.animal, ani.peso)}")

    def cantAdultos(self):
        cant = 0
        for ani in self.jaula:
            if ani.esAdulto():
                cant += 1
        return cant


print('Jaula de los Pumas')
jaula1 = Jaula("puma", 3)
jaula1.mostrarJaula()
print(f"Cantidad de adultos: {jaula1.cantAdultos()}")

print('Jaula de los Venados')
jaula2 = Jaula("venado", 2)
jaula2.mostrarJaula()