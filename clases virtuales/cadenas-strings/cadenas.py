
nombresCompletos = ['Cometto, Federico', 'Lerda, Tomas', 'Lopez, Manuel', 'Saby, Lucas', 'Saby, Adrian']

for i in range(len(nombresCompletos)):
    nombreCompleto = nombresCompletos[i]
    posComa = nombreCompleto.find(',')
    posInicial = posComa + 2
    inicial = nombreCompleto[posInicial]
    apellido = nombreCompleto[:posComa]
    nombre = nombreCompleto[posInicial:]  # tambien puedo poner  nombreCompleto[posComa+2:]
    nuevo_nombre = inicial + '. ' + apellido
    #print(nombre)
    print(nuevo_nombre)
    

#otro ejemplo

n = 'Spagnuolo, Facundo'
posiC = n.find(',')
letra_inicial = n[posiC + 2]
apell = n[:posiC]
nuevo = letra_inicial + '. ' + apell
print(nuevo)