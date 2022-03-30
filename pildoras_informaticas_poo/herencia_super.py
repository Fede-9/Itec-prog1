# Metodo super(): sirve para traer los metodos de la clase padre.

class Persona():
    def __init__(self,nombre,edad,lugarResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugarResidencia

    def descripcion(self):
        print(f'Nombre: {self.nombre}\nEdad: {self.edad}\nResidencia: {self.lugarResidencia}')


class Empleado(Persona):
    def __init__(self, nombre, edad, lugarResidencia, salario, antiguedad):
        super().__init__(nombre, edad, lugarResidencia) #ejecuta el metodo init de la clase padre
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion() #lamo al metodo de la clase padre
        print(f'Salario: {self.salario}\nAntiguedad: {self.antiguedad}')
        



fede = Empleado('Federico',23,'Serrano',150000,25)
fede.descripcion()
print(isinstance(fede,Empleado)) #para comprobar si nuestro es de determinada clase, devuelve True o False
