from dataclasses import dataclass


@dataclass  # este decorador nos ahorra escribir un constructor y agrega métodos
class Sportsman:
    nombre: str
    altura: float
    peso: float

    def __str__(self):  # ni falta que hace, sin esta igual imprime legible
        return f"{self.nombre}: {self.altura}m. de alto, {self.peso} kg. de peso"


deportista1 = Sportsman("Elena", 1.81, 64)
print(deportista1, type(deportista1))

atleta = str(deportista1)
print(atleta, type(atleta))


@dataclass(order=True, frozen=True)
class Deportista:
    nombre: str = "Desconocido"
    altura: float = 0
    peso: float = 0


deportista1 = Deportista(peso=64)
# deportista1.nombre = "Elena" # Da error si frozen=True
deportista2 = Deportista(peso=62)
deportista3 = Deportista(peso=67)

print(deportista1 > deportista2)  # True
print(deportista1 > deportista3)  # False