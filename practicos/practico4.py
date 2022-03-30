# Tenemos un archivo deudores.txt con información de personas que adeudan dinero.

# Necesitamos saber el nombre, la dirección de correo y el saldo de todos los que deben más de doscientos mil
#  pesos y cuya deuda sea del año pasado.

# Hacer:
# Recorrer el archivo deudores.txt y grabar uno nuevo llamado morosos.txt con los datos requeridos. 
# Para los saldos, el nuevo archivo NO tiene que tener el signo pesos ($) ni los centavos.
# El nuevo archivo tiene que tener cabecera en la primera línea con los nombres de los datos, similar 
# al archivo deudores.txt.



archiv = open('deudores.txt', 'r', encoding='utf-8' )   #para que interprete todos los caracteres sino no lo habre
lectura = archiv.readlines() #lee todo y guarda en una lista de strings por fila
#print(lectura)
lectura.pop(0)  #elmina la fila de titulos / puedo guardar en una variable y reutilizarlo
archiv.close()

    
nuevo = open('morosos.txt', 'w')
nuevo.write('nombre, mail, saldo\n')
for leer in lectura:
    lista = leer.split(',')
    nombre = lista[1]
    correo = lista[2]
    dinero = int(lista[4][1:-3]) # quito el signo $ y los centavos.
    fecha = int(lista[5][-4:])  # obtengo el año que es lo que necesito.
    if dinero > 200000 and fecha == 2019:
        nuevo.write(nombre + ', ' + correo + ', ' + str(dinero) + '\n')
        
nuevo.close()
        