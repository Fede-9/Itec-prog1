# 11. Ingresar la lluvia caída en milímetros para cada día de la semana.
#  Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

dias = ['domingo', 'lunes', 'martes', 'miercoles','jueves','viernes','sabado']

def cargarLluvias(lista):
    for i in range(7):
        print('Ingrese la lluvia del dia:',dias[i])
        lista.append(int(input()))
    return lista

def lluviaTotal(lista):
    total = 0
    for i in range(len(lista)):
        total = total + lista[i]
    return total

def mayorLluvia(lista):
    mayor = 0
    pos = 0
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            pos = i
    return pos

rioCuarto = []
cargarLluvias(rioCuarto)
totalRain = lluviaTotal(rioCuarto)
moreRain = mayorLluvia(rioCuarto)
print('-- LLUVIA TOTAL --')
print(totalRain)
print('-- DIA QUE MAS LLOVIO --')
print('{} con {} mms'.format(dias[moreRain], rioCuarto[moreRain]))