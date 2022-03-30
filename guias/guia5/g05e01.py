#En los primeros 5 ejercicios trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, 
# considerar que
#  una palabra es toda secuencia de caracteres diferentes de los separadores (los caracteres separadores 
# son el espacio, la coma y el punto).

#1. Cuántas veces se repite una letra cualquiera pedida. Parámetros: letra, cadena.

def contarLetra(letra,cadena):
    c = 0
    for e in cadena:
        if e == letra:
            c += 1
    return c

cad = "Quiero comer manzanas, solamente manzanas."
let = input("Ingrese una letra para saber cuantas veces se repite: ")
#let = 'a'   
print(f'La cantidad de veces que se repite su letra {let} es:  {contarLetra (let,cad)}')
