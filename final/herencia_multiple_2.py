class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Encargado():
    def __init__(self, codigo, departamento):
        self.codigo = codigo
        self.departamento = departamento


class Estudiante(Persona):
    def __init__(self, nombre, edad, clave, calificacion):
        # super().__init__(nombre, edad)
        # tambien se puede hacer de esta manera
        Persona.__init__(self, nombre, edad)
        self.clave = clave
        self.calificacion = calificacion


class EstudianteEncargado(Persona, Encargado):
    def __init__(self, nombre, edad, clave, calificacion, codigo, departamento):
        # super().__init__(nombre, edad)
        # tambien se puede hacer de esta manera
        Persona.__init__(self, nombre, edad)
        Encargado.__init__(self, codigo, departamento)
        self.clave = clave
        self.calificacion = calificacion
        self.codigo = codigo
        self.departamento = departamento




juan = Persona('Juan',15)
print(juan.nombre)


fede = Estudiante('Federico',24,'1998',10)
print(fede.clave)


estudianteEncargado1 = EstudianteEncargado('Lucas',21,'1999',10,'0001','Campo')
print(f'Nombre del estudiante encargado: {estudianteEncargado1.nombre}')
print(f'Departamento: {estudianteEncargado1.departamento}')