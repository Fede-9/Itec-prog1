
class Curso():
#     nombre = 'Matematica'
#     creditos = 5
#     profesion = 'Ingenieria civil'

#estado inicial del objeto
    def __init__(self, nombre, creditos, profesion):
        self.nombre = nombre
        self.creditos = creditos
        self.profesion = profesion



curso1 = Curso('Matematica',5,'Ingenieria civil')
curso2 = Curso('Lenguaje',4,'Ingenieria industrial')
print(curso1.nombre)
print(curso2.profesion)

