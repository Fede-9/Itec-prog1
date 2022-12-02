# HERENCIA MULTIPLE Y ATRIBUTOS CON SUPER

# Si hasta ahora vimos como heredar atributos de clases con Herencia Simple y como heredar Métodos con Herencia Múltiple. 
# Pero que pasa con los atributos en la Herencia Múltiple?. Pues super() no nos sirve en ese caso. 
# Debemos llamar a los constructores de ambas clases especificandolas por su nombre. 
# Y si cambiamos el nombre u orden de la clase deberemos especificarlo!



class Padre(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas


class Madre(object): #Creamos la clase Madre
    def __init__(self, brazos, piernas): #Definimos los Atributos
        self.brazos = brazos
        self.piernas = piernas
        

class Hijo(Padre, Madre): #Creamos clase hija que hereda de Padre y luego de Madre
    def __init__(self, ojos, cejas, cara, brazos, piernas): #creamos el constructor de la clase especificando atributos
        Madre.__init__(self, brazos, piernas)
        Padre.__init__(self, ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara
        

Tomas = Hijo('Marrones', 'Negras', 'Larga', 2, 2)
print (Tomas.ojos, Tomas.cejas, Tomas.cara, Tomas.piernas, Tomas.brazos)