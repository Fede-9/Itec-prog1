# 13. Pedir el ingreso de un nombre completo en la forma <nombre> <apellido>
# (ejemplo: Juan Pérez) y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan).

nombreCompleto = input('Ingrese su nombre y apellido: ')
nombre = nombreCompleto.title()  #mayuscula en la primera letra de cada palabra
nombre1 = nombre.split() #convierto en lista
nombre1.reverse()
invertido = ', '.join(nombre1) #convierto la lista en cadena.
print(invertido)

#OTRA FORMA DE HACERLO

name = input('Ingrese nombre y apellido separado por espacio: ')
nameSplit = name.split(' ')
invertido = nameSplit[1] + ', ' + nameSplit[0]
print(invertido)