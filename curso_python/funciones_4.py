# Crear una funcion que cuente la cantidad de vocales en una palabra dada



def contador_vocales(palabra):
    
    total_vocales = 0
    for letra in palabra:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            total_vocales += 1 

    return total_vocales

resultado_1 = contador_vocales('arbol') 
print('La cantidad de vocales es: ', resultado_1)


print('------------------')


resultado_2 = contador_vocales('escalera') 
print('La cantidad de vocales es: ', resultado_2)

