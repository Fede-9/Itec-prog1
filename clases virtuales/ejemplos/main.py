import funcs           #Tambien puedo importar cualquier modulo echo pormi con el import y asi 
print(funcs.saludo)    #puedo acceder a cualquier objeto que tenga en otro modulo, en este ejemplo los 
                         #objetos dentro de funcs.

from funcs import saludo,pi  #otra forma de traer objetos de otro modulo
print(saludo,pi)