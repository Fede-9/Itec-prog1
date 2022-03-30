# 9) Redefinir la clase auto con los atributos marca, modelo y año. Hacer una clase heredera TuAuto 
# que agrega dueño y color. 
# Hacer un método que devuelve el color y en el programa principal preguntar por un color y mostrar 
# sólo los autos que cumplan esa condición.

class Auto():
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

class TuAuto(Auto):
    def agregar(self,dueño,color):
        self.dueño = dueño
        self.color = color
        return self.dueño,self.color

    def devolverColor(self):
        if self.color == color1:
            return self.marca,self.modelo

    
persona1 = TuAuto('Ford','Focus',1998)
persona1.agregar('fede','rojo')
color1 = input('ingrese color: ')
print(persona1.devolverColor())


