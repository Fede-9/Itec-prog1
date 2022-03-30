numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #Creamos la lista con números
for num in numeros:     # En la variable "num" almacenamos los ítem de la lista
    if num % 2 == 0:    # Condición: Si el resto de la división por dos es cero entonces:
        print (num)     # Imprimimos la variable num

print('---------------------------------------------------')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  #Creamos la lista con números
for num in numeros:     # En la variable "num" almacenamos los ítem de la lista
    if num % 2 != 0:    # Condición: Si el resto de la división por dos es distinto a cero entonces:
        print (num)     # Imprimimos la variable num

print('------------------------------------------------------')


Palabras = ['Peine', 'Pelo', 'Ventana', 'Refrigerador', 'Adolescente', 'Dentista', 'Asesino'] 
for caracteres in Palabras:      #Creamos el bucle para iterar Palabras y almacenar en caracteres
    print ((caracteres), ('Longitud:'), (len(caracteres))) 


print('-----------------------------------------------')


entrada = "hola estoy programando en python"      #Cadena de texto a analizar
contador = 0
cuentalaletra = 'a'                               #Almacenamos en la variable la letra que queremos contar
for letra in entrada:                             #Almacenamos en letra cada ítem de la cadena
    if letra == cuentalaletra:                    #Si el ítem es igual a la letra a contar
        contador += 1                   #Sumamos uno al contador
    
print (f'La letra a se encuentra: {contador} veces')   

