# 2) Escriban un segundo programa que tendrá como salida los nombres de los mayores de edad. 
# Para ello, deberán leer el archivo creado en el punto 1 y reutilizar la o las funciones que hayan escrito para la salida original.

from calcula_edad import edad

f = open('data.txt', 'r')
personas = f.readlines()   #construye una lista en donde cada linea del archivo es un elemento de la lista.
print(personas)
for persona in personas:
    if edad(persona[-11:-1]) >= 18:    #porque la fecha tiene 10 caracteres mas la \n es 11 y voy hasta el -1 para sacar la \n
        print(persona[:-13]) #voy desde el guion hasta el inicio



#Otra forma de hacerlo

for persona in personas:
    posGuion = persona.find('-')
    nombre = persona[:posGuion]
    fn = persona[posGuion+2:-1]  #quito el salto de liña
    if edad(fn) >= 18:
        print(nombre)

