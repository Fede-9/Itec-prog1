class Persona():
    especie = "humana" # atributo de clase
    #self representa al objeto en sí mismo
    def __init__(self, nombre, edad): # Constructor (se ejecuta al crear un objeto)
        self.nombre = nombre # atributo de instancia
        self.edad = edad # atributo de instancia

    def obtenerDatos(self): # método
        return self.nombre, self.edad

    def obtenerNombre(self):
        return self.nombre


    def obtenerEdad(self):
        return self.edad > 12

   


# instanciaciones (instancia = objeto)
persona1 = Persona('John', 33) # Se crea un objeto de la clase Persona
persona2 = Persona('Jane', 22) # los argumentos los recibe el constructor
print(Persona.especie)

print(persona1.obtenerDatos())
print(persona2.nombre) # Se accede a los atributos de la clase violando el encapsulamiento

print(f'Nombre de la persona: {persona1.obtenerNombre()}')
print(persona1.obtenerEdad())