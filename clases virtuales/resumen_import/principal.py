#FORMAS DE IMPORTAR MODULOS
import mimodulo

resultado = mimodulo.sumar(7, 5)
print(resultado)
print(mimodulo.pi)

print('------- OTRA FORMA DE IMPORTAR UN MODULO --------')

from mimodulo import sumar, pi
resultado = sumar(7, 5)
print(resultado)
print(pi)

