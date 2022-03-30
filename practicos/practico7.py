# Dado el archivo de texto practico7.json, obtener:
# 1) Nombres y correos electrónicos de las personas cuyo dominio no sea .com
# 2) La cantidad de personas por país
# 3) El nombre del idioma hablado por la mayor cantidad de personas

from json import loads

f = open('practico7.json', 'r')
a = f.read()
f.close()
d = loads(a)  #convierto en una lista de diccionario

# ACTIVIDAD Nº1




# ACTIVIDAD Nº2

paises = {}
for e in d:
    pais = e['Location']['country']
    if pais not in paises.keys():
        paises[pais] = 1
    else:
        paises[pais] += 1


#paises = dict(sorted(paises.items(), key=lambda x: x[1], reverse=True))
print('Persona por pais')
for k, v in paises.items():
    print(k, ":", v)

from collections import Counter
lang = []
for e in d:
    lang.extend(e['languages'])
#print(lang)
d = dict(Counter(lang))
#print(d)
maxi = max(d.values())

def getKeys(dic, value):
    return [key for key, val in dic.items() if val == value]

print(maxi, 'personas hablan:')
for i in getKeys(d, maxi):
    print(i)