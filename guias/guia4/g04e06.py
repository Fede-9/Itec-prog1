#En los siguientes ejercicios (6 a 11) trabajamos con el texto:
#  “Quiero comer manzanas, solamente manzanas.”, considerar que una palabra es
#  toda secuencia de caracteres diferentes de los separadores
#  (los caracteres separadores son el espacio, la coma y el punto).

#6-Buscar una palabra completa en un texto y contar cuántas veces está.

cadena = 'Quiero comer manzanas, solamente manzanas.'
print(cadena)
usuario = input('Que palabra desea buscar? ')
ocurrencia = cadena.count(usuario)
print(f'La palabra se encuentra: {ocurrencia} veces')


lista = cadena.split()
cont=0
for i in range(len(lista)):
    if lista[i] == usuario or lista[i] == usuario + ',' or lista[i] == usuario + '.':
        cont+=1
    

print(f'La palabra - {usuario} - se encuentra: {cont} veces')
