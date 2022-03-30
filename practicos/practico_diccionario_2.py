# A partir de las estructuras de datos obtenidas en el ejercicio anterior, mostrar los nombres de las
# mujeres menores a 55 años y los nombres de los varones más altos que 1.85 metros.


leerContinuacion = open('continuacion.txt', 'r')
datos = leerContinuacion.readlines()
#print(datos)
leerContinuacion.close()


mujeres = datos[1] #mirar print de datos / en el subindice 1 se encuentran las mujeres.
varones = datos[0] #mirar print de datos / en el subindice 0 se encuentran los varones.
varones = eval(varones)  #paso de str a una lista de dict
mujeres = eval(mujeres)  #paso de str a una lista de dict
#print(mujeres)
#print(varones)

# 1
nombreM = ''
for e in range(len(mujeres)):
    nombreMujer = mujeres[e]['names']
    edadMujer = mujeres[e]['ages']
    if edadMujer < 55:
        nombreM += '\n' + nombreMujer 
        
print(f'Nombre de mujeres menores a 55 años: {nombreM}')
    


    
# 2
nombreV = ''
for i in range(len(varones)):
    nombreVaron = varones[i]['names']
    alturaVaron = varones[i]['heights']
    if alturaVaron > 1.85:
        nombreV += '\n' + nombreVaron 
    
print(f'Nombre de los varones mas altos que 1.85 metros: {nombreV}')

