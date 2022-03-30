#Pedir edad y peso de personas.
#Mostrar los nombres de los menores de edad que pesen mas de 80 kilos.

nombre = input('ingrese su nombre: ')

validado = False
while not validado:
    edad = input('ingrese su edad: ')
    try:    
        edad = int(edad)
        validado = True
    except:
        print('Error, debe ingresar un numero entero!!')



validado = False
while not validado:
    peso = input('ingrese su peso: ')
    try:    
        peso = int(peso)
        validado = True
    except:
        print('Error, debe ingresar un numero entero!!')

if edad < 18 and peso > 80:
    print(nombre)