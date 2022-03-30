#un objeto es una instancia de la clase
# herencia,polimorfismo y encapsulamiento(no funciona en python)
class Persona:
    
    nombre: str  #atributos
    edad: int

    def habla(self):  #metodos
        print('bla bla')

p = Persona() #instanciacion
p.habla()