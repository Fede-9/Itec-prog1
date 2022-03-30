# 2) Usando la biblioteca json


from json import loads

def cleanNumber(s):
    n = ''
    for c in s:
        if c.isdigit():
            n += c
    return n

def buildCSVline(*args):
    line = ''
    for e in args:
        line += e + ','
    line = line[:-1] + '\n'
    return line

f = open('pelis.json', 'r')
stringDeJson = f.read()
f.close()
listaDeDiccionarios = loads(stringDeJson)  #el loads convierte el gran strings que es el json en un diccionario
f = open('pelis.csv', 'w')
f.write('Nombre,Actor,Rating,Recaudacion\n')
for diccionario in listaDeDiccionarios:
    title = diccionario['Title']
    actor = diccionario['Actors'].split(',')[0] #para obtener el nombre del primer actor
    rating = diccionario['Ratings'][1]['Value'][:-1]  #pongo el sunindice 1 porque esta dentro de otro diccionario.
    caja = cleanNumber(diccionario['BoxOffice'])
    f.write(buildCSVline(title, actor, rating, caja))
f.close()