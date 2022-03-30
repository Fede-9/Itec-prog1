#Pedir edad y peso de personas.
#Mostrar los nombres de los menores de edad que pesen más de 80 kilos.

def vali(mensaje):
    validado = False
    while not validado:
        edad = input(mensaje)   #En lugar de edad le puedo poner cualquier nombre no afecta en nada.
        try:    
            edad = int(edad)                
            return edad
        except:    
            print('Error, debe ingresar un numero entero!!')


nombre = input('ingrese su nombre: ')
edad = vali('Ingrese edad: ')
peso = vali('Ingrese peso: ')
print(edad, peso)

#if edad < 18 and peso > 80:
 #   print(nombre)




