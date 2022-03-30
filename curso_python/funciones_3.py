# Ejemplos de funciones un poco mas complejas


# Vamos a crear una funcion la cual va a devolver True si el string/palabra tiene menos de 8 letras, si tiene mas
# de 8 letras, va a devolver False


def max_8_caracteres(palabra):
    
    total_letras = len(palabra) 
    if total_letras < 8: 
        return True
    else:
        return False
    
    
resultado = max_8_caracteres(palabra = 'arbol') # resultado = True
print('El resultado de la palabra es: ', resultado)

print('--------------------')

resultado_2 = max_8_caracteres(palabra='palindromo') # resultado = False
print('El resultado de la palabra es: ', resultado_2)