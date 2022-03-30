# POO - CLASES, ATRIBUTOS Y METODOS
class Persona():   #clase
    nombre = ''    #atributos
    apellidos = ''
    telefono = ''
    dni = ''
    sexo = ''

    def __init__(self, nombrex, apellidos, dni): #constructor 
        self.nombre = nombrex
        self.apellidos = apellidos
        self.dni = dni

    def saludar(self): # metodo
        saludo = 'Holaa, mi nombre es: ' + self.nombre
        return saludo


class Planilla(Persona):   #herencia
    salario = 15000
    moneda = 'dolares'

    def miSalario(self):
        msj = 'Mi salario es de: ' + str(self.salario)
        return msj


p1 = Planilla('Fede','Cometto', '121221')
print(p1.saludar())
print(p1.miSalario())
p2 = Persona('Maxi', 'Vilarrino', '54545454')
print(p2.saludar())
