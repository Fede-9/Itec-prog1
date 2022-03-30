class Persona(): #mayuscula por convecion / los parentesis no son obligatorios
    
     
    def __init__(self, nombre, edad): #metodo / el self quiere decir 'si mismo' / el self va a representar a cada objeto
        self.nombre = nombre
        self.edad = edad
        

    def getData(self):
        return self.nombre, self.edad

persona1 = Persona('Adán', 123) #instanciacion / creacion del objeto
persona2 = Persona('Eva', 101)


print(persona1.getData())
print(persona1.nombre) #violando el encapsulamiento
print(persona1.edad) #violando el encapsulamiento


print(persona2.getData())
print(persona2.nombre) #violando el encapsulamiento
print(persona2.edad) #violando el encapsulamiento