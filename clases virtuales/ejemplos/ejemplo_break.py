

while True: #Creamos el ciclo infinito
    opcion = (input("""Elige una fruta para tu desayuno: 
    1- Manzanas
    2- Bananas
    3- Nada
    """))#Creamos un input para que el usuario ingrese su opción y la almacenamos en "opcion"
       
    if opcion == '1': #Condicionales según la opción que eligió!
        print ("Has seleccionado manzanas")
        break #Rompemos el bucle
    elif opcion == '2':
        print ("Has seleccionado bananas")
        break #Rompemos el bucle
    elif opcion == '3':
        print ("Has seleccionado nada")
        break #Rompemos el bucle
    else:
        print ("Debes seleccionar una opcion (1, 2 o 3)")
print("Programa terminado, que disfrutes tu desayuno") #Agregamos un print FUERA DEL BUCLE dar fin
        
     