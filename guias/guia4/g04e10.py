#En los siguientes ejercicios (6 a 11) trabajamos con el texto:
#  “Quiero comer manzanas, solamente manzanas.”, considerar que una palabra es toda secuencia de 
# caracteres diferentes de los separadores (los caracteres separadores son el espacio, la coma y el punto).

# 10. Determinar cuál es la vocal que aparece con mayor frecuencia.

cadena = 'Quiero comer manzanas, solamente manzanas.'
a = cadena.count('a')
e = cadena.count('e')
i = cadena.count('i')
o = cadena.count('o')
u = cadena.count('u')

if a > e and a > i and a > o and a > u:
    print('la vocal que se repite con mayor frecuencia es la: a')
    print('se repite', a, 'veces')
if e > a and e > i and e > o and e > u:
    print('la vocal que se repite con mayor frecuencia es la: e')
    print('se repite', e, 'veces')
if i > a and i > e and i > o and i > u:
    print('la vocal que se repite con mayor frecuencia es: i')
    print('se repite', i, 'veces')
if o > a and o > e and o > i and o > u:
    print('la vocal que se repite con mayor frecuencia es: o')
    print('se repite', o, 'veces')
if u > a and u > e and u > i and u > o:
    print('la vocal que se repite con mayor frrecuenci es: u')
    print('se repite', u, 'veces')

print('-------------------------------------------------------------')




#OTRA FORMA DE HACERLO

frase = 'hola como andas pibe'
vocales = 'aeiou'
lista = [frase.count(v) for v in vocales]
print(lista)
for i in range(len(lista)):
    if lista[i] == max(lista):
        print(vocales[i])




#OTRA FORMA DE HACERLO

contar=[]
for x in vocales:
    contar.append(frase.count(x))

for z in range(len(contar)):
    if contar[z] == max(contar):
        print(f'La vocal que aparece con mas frecuencia es la: {vocales[z]} se repite {contar[z]} veces')
