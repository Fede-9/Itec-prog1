def dup(n):
    return n * 2
print(dup(5))

def saludar(nombre):
    print(f'Hola {nombre}')

saludar("mundo")

print('--------------------')

def sumar(a, b):
    return a + b

print(sumar(5,4))

print('------------------')

# Ahora bien, una función puede tener argumentos con valores por defecto, de modo que, al llamarla, si no 
# hemos especificado un valor concreto por argumento, éste toma automáticamente el que la definición le ha asignado por defecto.

def sumar(a, b=5):
    return a + b

# ¡Perfecto! Imprime 12.
print(sumar(7))
# En este caso, b == 10.
print(sumar(5, 10))


print('--------------------')

#Agreguemos, para avanzar un poco más, un tercer argumento c con un valor por defecto.

def sumar(a, b=5, c=10):
    return a + b + c

# Imprime 22 (7 + 5 + 10).
print(sumar(7))


#¿Qué ocurre si quiero indicar un valor para el argumento c mientras que b mantenga su valor por defecto?
#  En ese caso, en lugar de pasar el argumento por posición, lo voy a pasar por nombre.

# Imprime 32 (7 + 5 + 20).
print(sumar(7, c=20))

# La posibilidad de pasar argumentos por su nombre en la llamada a una función solo puede darse
#  en aquellos que tengan un valor por defecto. De ahí que a estos se los conozca como argumentos por nombre.
#  En estos casos, la posición de los argumentos es indistinta, de modo que el siguiente código es perfectamente válido.

# El orden es indistinto en los argumentos por nombre.
print(sumar(7, c=20, b=10))


print('--------------------')
#Cuando diseñamos una función, lo ideal es documentar su comportamiento utilizando comillas triples inmediatamente luego de su definición.

def dup(n):
    """
    Retorna el doble de `n`.
    """
    return n * 2

print(help(dup))   #imprime la documentacion por pantalla
print(dup(5))