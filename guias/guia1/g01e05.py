#5- Leer dos numeros reales y mostrarlos en orden creciente.
numero1 = int(input("escriba un numero: "))
numero2 = int(input("escriba otro numero: "))
orden_creciente = []
if numero1 > numero2:
    print(numero2, numero1)
elif numero1 < numero2:
    print(numero2, numero1)
else:
    print('Los numero son iguales')
    

    