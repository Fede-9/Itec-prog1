# ESTO ES UNA LISTA POR COMPRENSION:
# a, m, d = [int(e) for e in fecha.split('-')]

# ES LO MISMO QUE HACER:

lista = []
fecha = '1998-07-28'
for e in fecha.split('-'):
    lista.append(int(e))
a, m, d = lista

print(lista)
print(a)
print(m)
print(d)