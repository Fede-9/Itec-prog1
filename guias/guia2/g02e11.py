#Ingresar 7 números enteros y en el caso de que sean naturales de una sola cifra mostrar un 
# cartel en cada uno.

for x in range(1,8):
    numero = int(input("ingrese un numero entero: "))
    if numero > 0 and numero < 10:
        print("numero de una sola cifra !!")
    elif numero == 0:
        print('El numero es cero !!')
    elif numero < 0:
        print('El numero es negativo !!!')
    else:
        print('numero mayor a una cifra !!')

