#En los primeros 5 ejercicios trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”, considerar que
#  una palabra es toda secuencia de caracteres diferentes de los separadores (los caracteres separadores son el espacio, la coma y el punto).
# 2. Buscar una palabra y reemplazarla por otra todas las veces que aparezca.
# Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.'

def remplazo(palabra, cadena):
    cambio = cadena.replace("manzanas", palabra)
    return cambio

texto = "Quiero comer manzanas, solamente manzanas."
ingreso = input("Ingrese una palabra: ")
print(remplazo(ingreso,texto))

#OTRA FORMA DE HACERLO

t = 'Quiero comer manzanas, solamente manzanas.'
v = 'manzanas'
n = 'peras'


def remplazar(vieja, nueva, texto):
    while texto.find(vieja) != -1:
        posicion_vieja = texto.find(vieja)
        inicio = texto[:posicion_vieja]
        final = texto[posicion_vieja+len(vieja):]
        texto = inicio + nueva + final
    return texto

nueva_cadena = remplazar(v,n,t)
print(nueva_cadena)

otra_cadena = remplazar('River','Boca','River es el mejor equipo de la Argentina')
print(otra_cadena)