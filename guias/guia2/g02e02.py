#Preguntar si hay datos para ingresar, en caso afirmativo solicitar 
# un número entero y decir si es negativo o no. Preguntar si repite.
dato_1 = input("Desea ingersar algun dato?: ")

while dato_1 == "si":
    dato_2 = int(input("Ingrese un numero entero: "))
    if dato_2 >= 0:
        print("El numero es positivo")  
    else:
        print("El numero es negativo")
    dato_1 = input("Desea ingresar otro dato?: ")

print("fin..")