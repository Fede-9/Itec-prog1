# La instrucción continue dentro de un bucle obliga al
#  interprete a volver al inicio del bucle obviando todas las instrucciones o iteraciones debajo de el.


while True: #Creamos el ciclo infinito
    opcion = (input("""Elige una fruta para tu desayuno: 
    1- Manzanas
    2- Bananas
    3- Nada
    """))#Creamos un input para
        #que el usuario ingrese su opción y la almacenamos en "opcion"
        
############################################-2-##################################################       
    if opcion == '1': #Condicionales según la opción que eligió!
        print ("Has seleccionado manzanas")
        continue 
    elif opcion == '2':
        print ("Has seleccionado bananas")
        continue 
    elif opcion == '3':
        print ("Has seleccionado nada")
        continue 
    else:
        print ("Debes seleccionar una opcion (1, 2 o 3)")
