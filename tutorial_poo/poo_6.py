# CONSTRUCTOR


class Persona():
    pass
    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año
    
    def descripcion(self):
        return f'{self.nombre} tiene {self.año} años'

    def comentario(self,frase):
        return f'{self.nombre} dice {frase}'

doctor = Persona('Federico',23)
print(doctor.descripcion())
print(doctor.comentario('Hola que tal??'))