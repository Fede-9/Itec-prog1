#Transformar la cadena "River vuelve a las copas", en la cadena "River vuelve a la copa".
#  Resolverlo recorriendo la cadena original como si fuera una lista.

b = "River vuelve a las copas"
z =(b.split('s'))
#print(z)

for i in range(len(z)):
    print(z[i])
   

#otra froma de hacerlo
x = ''

for i in range(len(b)):
    if b[i] != 's':
        x += b[i]

print(x)
