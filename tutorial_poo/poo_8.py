# HERENCIA 

class Pokemon():
    
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre,self.tipo)
    
class Picachu(Pokemon): # picachu es una clase hija de la clase pokemon
    def ataque(self,tipoAtaque):
        return '{} tipo de ataque: {}'.format(self.nombre,tipoAtaque)

class Charmander(Pokemon): #clase hija de la clase pokemon
    def ataque(self,tipoAtaque):
        return '{} tipo de ataque: {}'.format(self.nombre,tipoAtaque)


nuevoPokemon = Picachu('Boby','Electrico')
print(nuevoPokemon.descripcion())
print(nuevoPokemon.ataque('Impacto trueno'))
