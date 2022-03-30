from dataclasses import dataclass

@dataclass
class Language:
    name: str
    born: int



lang1 = Language("Python", 1989)
lang2 = Language(name="Elixir", born=2012)
print(lang1.name)
print(lang1.born)
print(lang2.name)
print(lang2.born)


#Sin el decorador, habríamos de hacerlo de la forma tradicional:

class Language:
    
    def __init__(self, name: str, born: int):
        self.name = name
        self.born = born


# Como se trata de una clase normal, podemos también agregar métodos:

from dataclasses import dataclass
import datetime

@dataclass
class Language:
    name: str
    born: int
    
    @property
    def years_since_born(self) -> int:
        return datetime.datetime.now().year - self.born

lang1 = Language("Python", 1989)
print(lang1.name, "fue creado hace", lang1.years_since_born, "años.")