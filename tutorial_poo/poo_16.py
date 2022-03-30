# PROPIEDADES

class Empleado():
    def __init__(self,nombre,salario):
        self.__nombre = nombre
        self.__salario = salario

    
    def getNombre(self):
        return self.__nombre

    def getSalario(self):
        return self.__salario

    
    def setNombre(self,nombre): 
        self.__nombre = nombre

    def setSalario(self,salario):
        self.__salario = salario

    
    
    def delNombre(self):
        del self.__nombre

    def delSalario(self):
        del self.__salario


empleado1 = Empleado('Federico',45000)
print(empleado1.getNombre())
print(empleado1.getSalario())
empleado1.setNombre('Tomás')



