#6- Leer dos números y luego una opción (puede ser '+' o '-'), y según la opción elegida realizar el cálculo.
numero1 = float(input("digame un numero: "))
numero2 = float(input("digame otro numero: "))
opcion = input("elija '+' o '-': ")
if (opcion == '+'):
    print(numero1 + numero2)
elif (opcion == '-'):
    print(numero1 - numero2)