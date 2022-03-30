d = {"sitio": "Recursos Python", "url": "recursospython.com"}

print('------ METODO DUMPS ---------')
# Aquí creamos un simple diccionario con dos pares clave-valor. 
# Para convertirlo a una cadena JSON, utilizamos la función dumps.

import json
json.dumps(d)
'{"url": "recursospython.com", "sitio": "Recursos Python"}' 


#comillas dobles / true-false ---> en minuscula a diferencia de python que son en mayuscula / en vez de none es null

print(json.dumps([None, True, False, 'Hola, mundo!']))


print('-------- METODO LOADS --------')
# Para decodificar una cadena en el formato JSON (es decir, convertirla a un objeto de Python), utilizamos loads.

data = json.loads('[null, true, false, "Hola, mundo!"]')
print(data)
print(data[1])
print(data[3])

print('----- OTRO EJEMPLO DE LOADS ------')

d = json.loads('{"url": "recursospython.com", "sitio": "Recursos Python"}')
print(d["url"])
print(d["sitio"])


print('###############################################################')
#  ¡¡¡¡¡¡ CODIFICAR Y DECODIFICAR EN ARCHIVOS !!!!!!

# Además, el módulo json provee las funciones dump y load, similares a dumps y loads pero que operan con archivos. 
# Por ejemplo, podemos almacenar una lista de Python en un archivo con el formato JSON:

data = [True, False, None, 'Hola, mundo!']
with open("data.json", "w") as f:
   json.dump(data, f)

# De forma análoga recuperamos el objeto leyendo el fichero vía load().

with open("data.json") as f:
    data = json.load(f)
# Imprime [True, False, None, 'Hola, mundo!'].
print(data)