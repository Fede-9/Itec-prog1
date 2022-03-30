print('------------ DICCIONARIO INICIAL -------------')
d = {"Python": 1991, "C": 1972, "Java": 1996}
print(d)


#Para acceder a alguno de los valores se indica su clave correspondiente entre corchetes.
print('----------- MOSTRAR EL VALOR DE UNA CLAVE -------------')
print(d['Python'])  
#Y bajo la misma sintaxis le asignamos un nuevo valor.
print('---------------- ASIGNAR NUEVO VALOR / AGREGAR UN NUEVO ELEMENTO ---------------------')
d["Python"] = 2001
print(d)
#También de esta forma podemos agregar nuevos elementos.
d["C++"] = 1983
print(d)

print('------- METODO KEYS ------------') #muestro las claves
clave = d.keys()
clave = d.keys()
print(clave)

print('-------- METODO VALUES ---------') #muestro los valores
valores = d.values()
print(valores)

print('---------- METODO ITEMS ---------') #muestro claves y valores
claveValor = d.items()
print(claveValor)



print('------------- METODO GET ------------')
#Una forma alternativa para obtener un valor es vía el método get(), indicándo la clave como argumento.
#De esta forma, cuando la clave no existe el valor retornado es None.
print(d.get("Python"))

print('------------ METODO DEL -------------')
#La palabra reservada del permite remover un valor.
del d["Python"] #elimino clave y valor
print(d)

print('------------- ITERAR DICCIONARIO / RECORRER SUS CLAVES  -----------')
#Al iterar un diccionario, éste retorna sus claves.

for clave in d:
    print(clave)

for clave in d.keys():
    print(f'Claveeee: {clave}')


print('------------- ITERAR DICCIONARIO / RECORRER SUS VALORES -----------')
#Para recorrer sus valores, se emplea el método dict.values().

for valores in d.values():
    print(valores)


print('-------- ITERAR DICCIONARIO / RECORRER CLAVES Y VALORES ---------------')
#Y para recorrer tanto claves como valores simultáneamente:

for claves, valores in d.items():
    print(claves,'---->', valores)


print('--------- METODO LEN ------------')
#Al tratarse de una colección, len() devuelve la cantidad de pares clave-valor que conforman el diccionario.

print(len(d))


print('######### OTRAS OPERACIONES ###########')

#Para determinar si una clave pertenece a un diccionario, se emplea la palabra reservada in.
"Python" in d


print('---------- METOD CLEAR --------')
#El método clear() elimina todas las claves y valores.

d.clear()
#(Aunque por lo general simplemente se crea un nuevo diccionario vía d = {}).


print('-------------- ACTUALIZAR O UNIR DICCIONARIOS --------')
#Podemos actualizar un diccionario ─ o bien unir dos de ellos ─ vía update().

d = {"Python": 1991, "C": 1972, "Java": 1996}
d2 = {"Elixir": 2011, "Ruby": 1995}
d.update(d2)
print(d)


print('------- FUNCION POP ------------')
#La función pop() es similar a get(), pero elimina el elemento una vez retornado.

d = {"Python": 1991, "C": 1972, "Java": 1996}
eliminado = d.pop("Python") 
print(eliminado)  #Al elemento eliminado lo pueddo guardar en una variable.
print(d)

print('-------- RETORNAR UN PAR CLAVE-VALOR ALEATORIO ---------')
# Por otro lado, popitem() retorna un par clave-valor de forma aleatoria
# (no podría ser de otra forma pues es una colección no ordenada), y luego lo remueve. 
# Invocar este método en un diccionario vacío lanza KeyError.
print(d.popitem())


print('------- OTRAS FORMAS DE CREAR DICCIONARIOS ---------')
# Haciendo uso directo de la clase dict Python ofrece algunos métodos para crear diccionarios de formas alternativas
#  (cuyo uso, por cierto, es poco usual).
# Si se pasan argumentos por nombre a dict(), constituirán las claves del nuevo diccionario como cadenas.
d = dict(Fede=1991, Lucas=1972, Ncolas=1996)
print(d)



