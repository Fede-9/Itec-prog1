#En los primeros 5 ejercicios trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, considerar que
#  una palabra es toda secuencia de caracteres diferentes de los separadores (los caracteres separadores son el espacio, la coma y el punto).

# 3. Contar la cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes).


def ContarLetra(cadena):
    c = 0
    for x in range(len(cadena)):
        
        if cadena[x] != " " and cadena[x] != "," and cadena[x] != ".": 
            c += 1
    return c

cad = "Quiero comer manzanas, solamente manzanas."
print("total de letras:", ContarLetra(cad))