vocales = ['A', 'E', 'I', 'O', 'U']
Nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel', 'Alejandro', 'Leonel', 'Antonio', 'Omar',
'Antonia', 'Amalia', 'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']
Nombresvocales = [nombre for nombre in Nombres if nombre[0] in vocales]
print (Nombresvocales)

#ES LO MISMO

Nombresvocales = []
vocales = ['A', 'E', 'I', 'O', 'U']
Nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel', 'Alejandro', 'Leonel', 'Antonio', 'Omar','Antonia', 'Amalia', 'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']
for nombre in Nombres: #Para el elemento nombre, iteramos la lista Nombres
    if nombre[0] in vocales: #Si el índice 0 del elemento nombre está en la lista vocales
        Nombresvocales.append(nombre)#Agregamos el nombre a la lista Nombresvocales
    
print (Nombresvocales)


#OTRO EJEMPLO

Listafemeninos = [] #Creamos la lista vacía
Listamasculinos = [] #Creamos la lista vacía
Nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel', 'Alejandro', 'Leonel', 'Antonio', 'Omar',
'Antonia', 'Amalia', 'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']
for nombre in Nombres: #Para el elemento nombre, iteramos la lista Nombres
    if nombre[-1] == 'a' or nombre[-1] == 'e': #Si el índice -1 del elemento nombre en Nombres es a o e
        Listafemeninos.append (nombre)#Agregamos el nombre a la lista Listafemeninos
    else:
        Listamasculinos.append (nombre)#Si no termina en a o e agregamos a Listamasculinos
print (Listafemeninos)
print ("-------------------")
print (Listamasculinos)


#ES LO MISMO

Nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel', 'Alejandro', 'Leonel', 'Antonio', 'Omar',
'Antonia', 'Amalia', 'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']
Listafemeninos = [nombre for nombre in Nombres if nombre[-1] == 'a' or nombre[-1] == 'e'] #Creamos la lista
Listamasculinos = [nombre for nombre in Nombres if nombre[-1] != 'a' and nombre[-1] != 'e'] #Creamos la lista
print (Listafemeninos)
print ("-------------------")
print (Listamasculinos)