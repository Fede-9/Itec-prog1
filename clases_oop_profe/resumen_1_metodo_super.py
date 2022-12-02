# METODO SUPER EN HERENCIA SIMPLE

# Esta función nos permite invocar y conservar un método o atributo de una clase padre (primaria) desde una clase hija (secundaria) sin tener que nombrarla explícitamente. Esto nos brinda la ventaja de poder cambiar el nombre de la 
# clase padre (base) o hija (secundaria) cuando queramos y aún así mantener un código funcional, sencillo  y mantenible.

class Padre(): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
        
class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos, el atributo cara es propio de la clase Hijo
        Padre.__init__(self, ojos, cejas) #Especificamos la clase y llamamos a su constructor + Atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo
        
Tomas = Hijo('Marrones', 'Negras', 'Larga')
print(Tomas.ojos, Tomas.cejas, Tomas.cara)


# O podemos hacerlo, utilizando super(). De esta forma es casi el mismo código pero no necesitamos especificar la clase padre, por lo 
# que podremos cambiarle el nombre en cualquier momento y nuestro código seguirá funcional, fíjate:

# SE RECOMIENDA EN HERENCIA SIMPLE UTILIZAR SUPER.



class Agregarelemento(list): #Creamos una clase Agregarelemento heredando atributos de clase list (clase incorporada)
    
    def append(self, alumno): #Definimos que el método append (de listas) añadirá el elemento alumno
        print (("Añadido el alumno"), (alumno)) #Imprimimos el resultado del método
        super().append(alumno) #Incorporamos la función super SIN INDICAR LA CLASE ACTUAL, seguida
                                                    #del método append para la variable alumno

Lista1 = Agregarelemento() #Definimos la clase de nuestra lista llamada "Lista1"
Lista1.append ('Matias') #Añadimos un elemento a la lista como lo haríamos normalmente
print (Lista1) #Imprimimos la lista para corroborar que se añadió el alumno


# En este caso cada vez que se añada un elemento a la lista se imprimirá el elemento que se añadió porque así lo definimos (mediante un print) 
# en la clase hija y mediante la función super logramos ejecutar el método (“append“) padre de la clase incorporada list.

