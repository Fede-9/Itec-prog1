class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print(self.nombre, self.edad)
    
        
class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def presentar(self):
        print(f'profesor de {self.asignatura}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentar(self):
        print(f'estudio {self.carrera}')



profe = Profesor('Pablo', 45, 'Programacion 1')
profe.hablar()
profe.presentar()

estudiante = Estudiante('Federico',24,'Desarrollo de Software')
estudiante.hablar()
estudiante.presentar()
