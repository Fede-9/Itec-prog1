#En los siguientes ejercicios (6 a 11) trabajamos con el texto: “Quiero comer manzanas, solamente manzanas.”
#considerar que una palabra es toda secuencia de caracteres diferentes de los separadores 
#(los caracteres separadores son el espacio, la coma y el punto).

#7-Buscar una palabra y reemplazarla por otra todas las veces que aparezca.
#Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.' Sin usar replace.

cadena = 'Quiero comer manzanas, solamente manzanas.'
vieja = 'manzanas'
nueva = 'peras'
posi = 0
while posi != -1:
    posi = cadena.find(vieja)
    if posi != -1:
        inicio = cadena[:posi]
        final = cadena[posi+len(vieja):]
        cadena = inicio + nueva + final
print(cadena)


#OTRA FORMA DE HACERLO

frase = input('Ingrese la frase: ')
print(frase)
palabra = input('Ingrese la palabra a buscar: ')
reemplazo = input('Por cual palabra desea reemplazarla?: ')
fraseSplit = frase.split(' ')
for i in range(len(fraseSplit)):
    if(fraseSplit[i].lower() == palabra.lower()):
        fraseSplit[i] = reemplazo 
    elif fraseSplit[i].lower() == palabra.lower() + '.':
        fraseSplit[i] = reemplazo + '.'
    elif fraseSplit[i].lower() == palabra.lower() + ',':
        fraseSplit[i] = reemplazo + ',' 
aux = ''
aux = ' '.join(fraseSplit)
print(palabra,'reemplazada por:',reemplazo)
print(aux)