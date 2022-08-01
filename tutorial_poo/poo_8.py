# HERENCIA 

class Pokemon():
    
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def descripcion(self):
        return f'{self.nombre} es un pokemonde tipo {self.tipo}'
        
    
class Picachu(Pokemon): # picachu es una clase hija de la clase pokemon
    def ataque(self,tipoAtaque):
        return f'{self.nombre} tipo de ataque: {self.tipoAtaque}'
       

class Charmander(Pokemon): #clase hija de la clase pokemon
    def ataque(self,tipoAtaque):
        return '{} tipo de ataque: {}'.format(self.nombre,tipoAtaque)


nuevoPokemon = Picachu('Boby','Electrico')
print(nuevoPokemon.descripcion())
print(nuevoPokemon.ataque('Impacto trueno'))
