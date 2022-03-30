from calcula_edad import edad

nombresCompletos = ['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio', 'Campoamores, Susana', 'Santamaría, Carlos', 'Skarsgard, Azul', 'Catalejos, Walter']
sexos = ['f','f','m','f','m','f','m']
fechas = ['02/05/1943', '07/09/1984', '10/02/1971', '21/12/1967', '30/01/1982', '30/08/1995', '18/07/1959']

def getNombresApellidos(lista):
    lNombres = []
    lApellidos = []
    for nombreCompleto in lista:
        posComa = nombreCompleto.find(',')
        nombre = nombreCompleto[posComa+2:]
        apellido = nombreCompleto[:posComa]
        lNombres.append(nombre)
        lApellidos.append(apellido)
    return lNombres, lApellidos

def mostrarInicialesPuntoApellidos(nombres, apellidos):
    for i in range(len(nombres)):
        nuevoNombreCompleto = nombres[i][0] + '. ' + apellidos[i]
        print(nuevoNombreCompleto)

def nombreMasLargo(nombres):
    largo = 0
    nombreLargo = ''
    for nombre in nombres:
        if len(nombre) > largo:
            largo = len(nombre)
            nombreLargo = nombre
    return nombreLargo

def promedioEdadMujeres(sexos, fechas):
    tE = 0
    cM = 0
    tt = 0
    for x in range(len(sexos)):
        tt += edad(fechas[x])
        if sexos[x] == 'f':
            tE += edad(fechas[x])
            cM += 1
    return tE//cM

nombres, apellidos = getNombresApellidos(nombresCompletos)

print('1- Iniciales y Apellido Completo')
mostrarInicialesPuntoApellidos(nombres, apellidos)
print('--------------------------------------')
print('Nombre más largo')
print(nombreMasLargo(nombres))
print('--------------------------------------')
print('Promedio de edad de las mujeres')
print(promedioEdadMujeres(sexos, fechas))