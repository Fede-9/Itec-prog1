from dataclasses import dataclass


@dataclass
class Animal():
    identificador: int
    peso: float

    def esSano(self):
        if self.peso >= self.pesoSano:
            return "sano"
        else:
            return "enfermo"


@dataclass
class Puma(Animal):
    edad: int
    pesoSano: float = 200

    def esAdulto(self):
        if self.edad >= 5:
            return True
        else:
            return False


@dataclass
class Venado(Animal):
    pesoSano: float = 120

    


@dataclass
class Jaula():
    animal: str
    cantidad: int

    def __post_init__(self): # Si no quieres que sea un parámetro , puedes usar el método __post_init__ el cual es ejecutado inmediatamente después del __init__
        self.jaula = []
        for x in range(self.cantidad):
            peso = int(input(f"Ingrese el peso del {self.animal}: "))
            if self.animal == "puma":
                edad = int(input(f"Ingrese la edad del {self.animal}: "))
                ani = Puma(x + 1, peso, edad)
            else:
                ani = Venado(x + 1, peso)
            self.jaula.append(ani)

    def mostrarJaula(self):
        for ani in self.jaula:
            print(f"{ani.identificador} - {ani.esSano()}")

    def cantAdultos(self):
        cant = 0
        for ani in self.jaula:
            if ani.esAdulto():
                cant += 1
        return cant


jaula1 = Jaula("puma", 3)
jaula1.mostrarJaula()
print(f"Cantidad de adultos: {jaula1.cantAdultos()}")

jaula2 = Jaula("venado", 2)
jaula2.mostrarJaula()