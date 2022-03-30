#con este metodo podemos validar una entrada

validado = False
while not validado:

    s = input('ingrese un numero: ')
    try:    #permite intentar ejecutar una instruccion
        n = int(s)
        validado = True
    except:
        print('Error, debe ingresar un numero entero!!')

print('El doble del numero ingresado es: ', n * 2)

