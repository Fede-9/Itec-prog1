#4- Leer dos numeros y decir cual es mayor.

numero1 = int(input("escriba un numero: "))
numero2 = int(input("escriba otro numero: "))
if (numero1 > numero2):
    print(numero1, "es mayor")
elif (numero1 == numero2):
    print("los numeros son iguales")
elif (numero1 < numero2):
    print(numero2, "es mayor")