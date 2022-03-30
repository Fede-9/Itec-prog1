#Pedir edad y altura de personas.
#Mostrar los nombres de los menores de edad que midan más de 1.80 metros.

def vali(tipo, mensaje):
    validado = False
    while not validado:
        edad = input(mensaje)   #En lugar de edad le puedo poner cualquier nombre no afecta en nada.
        try:
            if tipo == 'entero':    
                edad = int(edad) 
            elif tipo == 'real':
                edad = float(edad)               
            return edad
        except:    
            print('Error, debe ingresar un numero', tipo)


nombre = input('ingrese su nombre: ')
edad = vali('entero', 'Ingrese edad: ')
altura = vali('real', 'Ingrese su altura: ')
print(edad, altura)

