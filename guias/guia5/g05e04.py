#En los primeros 5 ejercicios trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, considerar que
#  una palabra es toda secuencia de caracteres diferentes de los separadores (los caracteres separadores son el espacio, la coma y el punto).

# 4. Contar la cantidad de palabras.


def ContarPalabra(cadena):
    c = 0
    for x in range(len(cadena)):
        
        if cadena[x] == " " :
            c += 1
    return c + 1

texto = "Quiero comer manzanas, solamente manzanas."
print("la cantidad de palabras es:", ContarPalabra(texto))



#OTRA FORMA DE HACERLO

def contadorPalabras(word):
    lista = word.split()
    cantPalabras = len(lista)
    return cantPalabras

frase = 'Quiero comer manzanas, solo manzanas.'
print('La frase ingresada tiene',contadorPalabras(frase),'palabras')