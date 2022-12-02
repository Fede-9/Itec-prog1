class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentacion(self):
        print(f'soy {self.nombre} y tengo {self.edad} años')


class Instituto():
    def __init__(self, nombreInstituto):
        self.nombreInstituto = nombreInstituto

    def presentacionItec(self):
        print(f'Estudio en el {self.nombreInstituto}')

      

class Estudiante(Persona, Instituto):
    def __init__(self, nombre, edad, nombreInstituto, asignatura):
        Persona.__init__(self, nombre, edad)
        Instituto.__init__(self, nombreInstituto)
        self.asignatura = asignatura

    def presentarse(self):
        print(f'soy {self.nombre} tengo {self.edad} años y estudio {self.asignatura} en el {self.nombreInstituto}')



est = Estudiante('federico', 24, 'itec', 'programacion')
est.presentarse()
est.presentacion()
est.presentacionItec()