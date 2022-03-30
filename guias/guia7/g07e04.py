# 4) Definir una clase Persona cuyo constructor reciba nombre y edad.
#  El programa principal pedirá en forma repetitiva (hasta que no haya más) los mismos datos, hará 
# la instanciación de un objeto y lo agregará en una lista.
#  Por lo tanto, los elementos de dicha lista serán objetos y podrá mostrarse por recorrido y/o por 
# subindicación.

class Persona():
    def __init__(self, nombre, edad): # el constructor recibe nombre y edad
        self.nombre = nombre
        self.edad = edad

    def getName(self):
        return self.nombre

    def getAge(self):
        return self.edad

if __name__ == "__main__":
    lista = []
    respuesta = "si"
    while respuesta == "si":
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        persona = Persona(nombre, edad)
        lista.append(persona)
        print("Persona agregada")
        respuesta = input("Agregar otra persona? (si/no) ")
        
    
    for persona in lista:
        print(persona.getName(), persona.getAge())