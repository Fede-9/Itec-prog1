#En los primeros 5 ejercicios trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, considerar que
#  una palabra es toda secuencia de caracteres diferentes de los separadores (los caracteres separadores son el espacio, la coma y el punto).

# 5.Averiguar qué cantidad de letras tiene la palabra más larga. 
#  Para ello, primero cargar cada palabra en una lista y luego obtener la solicitada.
#  Usar dos funciones.



cadena = "Quiero comer manzanas, solamente manzanas."

def ObtLisPal(cadena):
    Z = ""
    for x in range(len(cadena)):
        if cadena[x] not in (".,"):
            Z += cadena[x]
    Z2 = Z.split(" ")
    return Z2

li = ObtLisPal(cadena)
print(ObtLisPal(cadena))


def ContaLetPalMasLarga(lista):
    c = 0
    for i in range(len(lista)):
        if len(lista[i]) > c:
            c = len(lista[i])
    return c

print("cantidad de letras de la palabra mas larga es:", ContaLetPalMasLarga(li))



#REVISARRRRRRRR  , esto lo hizo el profe en clases

texto = "Quiero comer manzanas, solamente manzanas."


def armarLista(cadena):
    d = ''
    for w in cadena:
        if w not in ',.': # if l != ',' and l != '.'
            d += w
    return d.split(' ')

#print(armarLista(soga))

def masLarga(lista):
    c = 0
    for palabra in lista:
        if len(palabra) > c:
            c = len(palabra)
    return c

# print(masLarga(['hola', 'q', 'bernabeu', 'chau']))

print('La cantidad de letras de la palabra mas larga es',masLarga(armarLista(texto)))