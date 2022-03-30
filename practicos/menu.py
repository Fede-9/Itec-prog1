from funciones_cometto import inputRangeInt


def menu():
    op = 0
    while op != 3:
        print('1. Primera')
        print('2. Segunda')
        print('3. Salir')
        op = inputRangeInt('Opcion: ',1, 3)
        if op == 1:
            print('Opcion 1')  #aca puede estar la llamada de la funcion
        elif op == 2:
            print('Opcion 2')
        elif op == 3:
            print('Adios')

menu()