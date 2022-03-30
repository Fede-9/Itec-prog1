def f1():
    print('hola')
f1()

def f2():
    return 'chau'  #Lo que hace este return es asignarle ese valor de retorno al nombre de la funcion en si mismo.
x = f2()
print(x)



#Un parametro es algo similar a una variable que se coloca entre los parentesis de una funcion y permite 
# que uno le pase un argumento y que dentro de la funcion se va a comportar con el nombre del parametro.

#EL PARAMETRO ES EN EL MOMENTO DE LA DEFENICION
#ARGUMENTO ES EN EL MOMENTO DE LA EJECUCION

def f3(nombre):
    saludo = 'Hola' + nombre
    return saludo

n = ' Ana'
print(f3(n))       #Es lo mismo de ambas formas.
print(f3(' Ana'))


def f4(nombre, edad):
    saludo = 'Hola' + nombre + ' tenes ' + str(edad) + ' años '
    return saludo

n = ' Ana'
print(f4(n, 44 ))