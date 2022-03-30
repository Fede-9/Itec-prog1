# Se debe realizar el juego MILES.

# Este juego consiste en adivinar un número de 4 cifras que piensa la computadora.
# Dicho número no puede tener cifras repetidas y debe ser superior a 1000 (no puede comenzar con cero).

# El jugador va proponiendo números y el programa le contesta los aciertos:

# Si un dígito del usuario está en el número de la computadora la respuesta será:
# BIEN, si está en la misma posición
# REGULAR si está presente pero en otra posición

# Se termina al adivinar el número exacto y se debe almacenar en un archivo de texto el nombre del jugador y la cantidad 
# de intentos que le llevó ganar.
# El programa también debe permitir mostrar el top ten del ranking de jugadores, ordenados por 
# las sesiones con menor cantidad de intentos para el acierto.


from random import randint  #La función randint() devuelve un número entero incluido entre los valores indicados.

c = 0
n = []
while c < 4:
    z = randint(0 ,9)
    if str(z) not in n:
        n.append(str(z))
        c += 1

if n[0] == '0':
    x = randint(1, 3)
    n[0], n[x] = n[x], n[0]   #swap o intercambio
print(n)

win = False
intentos = 0
while not win:
    bien = 0
    regular = 0
    a = input('Numero: ')
    intentos += 1
    for x in range(4):
        if a[x] in n:
            if a[x] == n[x]:
                bien += 1
            else:
                regular += 1
    if bien == 4:
        win = True
    else:
        print(f'{bien} bien y {regular} regular. Intento = {intentos}')

if win:
    print(f'Acerto!! Numero: {"".join(n)}. Intentos: {intentos}')




