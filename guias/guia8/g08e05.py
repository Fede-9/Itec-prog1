# 5) Implementar la clase Asignatura que represente el nombre de una asignatura y la nota correspondiente obtenida. Las operaciones son:
# Constructor que acepte como parámetros el nombre de la asignatura y la nota obtenida.
# Métodos para modificar la nota (setNota) y para consultar la nota (getNota).
# Método que nos devuelva “Aprobado” si la nota es mayor o igual a 4 o “Reprobado” si la nota es menor que 4.
# Método para consultar el nombre de la asignatura.
# Implementar la clase Alumno que incluya una coleccion de Asignaturas a las que el alumno ha asistido. 
# Ademas de incluir los atributos nombre y edad. Las operaciones disponibles sobre el alumno son:
# Constructor que acepte como parámetro el nombre del alumno y edad.
# Métodos para modificar el nombre (setNombre) y para consultarlo (getNombre).
# Métodos para modificar y consultar la edad.
# Método que nos devuelva el promedio del alumno.
# Método para agregar una Asignatura a su plan de estudio; verificar que la asignatura no exista previamente en el arreglo de este Alumno.
# Implementar la clase Aplicación para hacer uso de las clases Alumno y Asignatura.
# Crear 3 alumnos (Tres instancias de la clase Alumno) con sus respectivos nombre y edad.
# Para cada alumno establecer sus asignaturas y la nota obtenida.
# Imprimir en pantalla:
# 1.Nombre del alumno.
# 2.Edad.
# 3.Asignaturas que cursó:
# Nombre de la asignatura.
# Nota obtenida.
# Si es una asignatura aprobada o no.
# 4.Promedio del alumno

class Asignatura():

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def setNota(self, nota):
        self.nota = nota
    
    def getNota(self):
        return self.nota
    
    def getCondicion(self):
        resul = ""
        if self.nota >=4:
            resul = "Aprobado"
        else:
            resul = "Reprobado"
        return resul
    
    def getNombre(self):
        return self.nombre


class Alumno():
    
    def __init__(self, nombre, edad):
        self.listaMaterias = []
        self.nombresMaterias = []
        self.nombre = nombre
        self.edad = edad
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def setEdad(self, edad):
        self.edad = edad
    
    def getEdad(self):
        return self.edad
    
    def addMateria(self, nombre, nota):
        
        if nombre not in self.nombresMaterias:
            materia = Asignatura(nombre, nota)
            self.listaMaterias.append(materia)
            self.nombresMaterias.append(nombre)
            
    def getMaterias(self):
        for m in self.listaMaterias:
            print(m.getNombre(), m.getNota(), m.getCondicion())
    
    def promedio(self):
        acum = sum([m.getNota() for m in self.listaMaterias])
        return acum / len(self.listaMaterias)


class App():

    def __init__(self):
        a1 = Alumno("Juan", 25)
        a2 = Alumno("Ana", 19)
        a3 = Alumno("Pepe", 21)

        a1.addMateria("Python", 10)
        a1.addMateria("Python", 2)
        a1.addMateria("Ingles", 8)
        a1.addMateria("Lengua", 3)
        a1.addMateria("Python", 9)

        print(a1.getNombre()) 
        print(a1.getEdad()) 
        a1.getMaterias()
        print(a1.promedio()) 

apli = App()
