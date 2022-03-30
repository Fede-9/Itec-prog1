class Estudiante():  #Creamos la clase padre

    def __init__(self, edad, nombre): # Definimos los parámetros edad y nombre
        self.edad = edad #Declaramos que el atributo edad es igual al argumento edad
        self.nombre = nombre #Declaramos que el atributo nombre es igual al argumento nombre

class Instituto():

    def presentarInstituto (self):
        print("Estudio en el ITEC")
        
class Programacion(Estudiante, Instituto): #Entre paréntesis indicamos la clase padre o principal ESTUDIANTE
                            #Lo que la convierte a PROGRAMACION en una clase hija o secundaria
    def presentarse(self): #Creamos el método presentarse
       print (f"Soy {self.nombre} tengo {self.edad} años y estudio Derecho") #Se presenta llamando los atributos
       
alumno1 = Programacion(23, 'Federico Cometto') #Indicamos argumentos edad y nombre
alumno1.presentarse() # Llamamos al método y Manuel se presenta
alumno1.presentarInstituto()

