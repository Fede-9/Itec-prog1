#Ingresar nombres en una lista, luego buscar un nombre y de encontrarlo decir en qué posición está.


preg1 = int(input('cuantos nombres desea ingresar? '))
nombres = []
nombre_buscado = []

for i in range(preg1):
    preg2 = input('ingrese un nombre: ')
    nombres.append(preg2)

for x in range(len(nombres)):
    if nombres[x] == 'federico':
        nombre_buscado.append([x])

print('nombres ingresados: ', nombres)
print('posicion del nombre federico: ',nombre_buscado)




#OTRA FORMA DE HACERLO

cant = int(input('Cuantos nombre quiere ingresar: '))
nom = []

for z in range(cant):
    n = input('Ingrese el nombre: ')
    nom.append(n)

busqueda = input('Ingrese nombre para buscar: ')
posi = []

for e in range(len(nom)):
    if busqueda == nom[e]:
        posi.append(e)
    else:
        print('no se encontro el nombre')

print(f'Posicion del nombre buscado: {posi}')