

i = 0              #Declaramos el valor de la variable "i"
while (i <= 9):    #Creamos el bucle con la condición de ejecutarse mientras "i"
    i +=1          #Cuerpo de la repetición = sumamos uno a i (i es igual a i mas uno)
    print (i)      #Imprimimos "i"
                   #sea menor o igual a "9"







print('-----------  CICLO INFINITO  -----------------------------')



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
    elif opcion == '2':
        print ("Has seleccionado bananas")
    elif opcion == '3':
        print ("Has seleccionado nada")
    else:
        print ("Debes seleccionar una opcion (1, 2 o 3)")



