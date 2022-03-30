#Ingresar 7 números enteros y en el caso de que sean naturales de una sola cifra mostrar un 
# cartel en cada uno.

for x in range(1,8):
    numero = int(input("ingrese un numero entero: "))
    if numero > 0 and numero < 10:
        print("numero de una sola cifra !!")
