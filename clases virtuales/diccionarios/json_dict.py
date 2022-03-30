from json import loads, dumps

j = '{"name": "John", "age": null, "active": true}' #estos es un objeto json dentro de un string de python / en el json siempre se usan comillas dobles 
k = loads(j) # convierte la string JSON en un diccionario de Python
print(k)

users = [
    {"user": "juan", "active": True, "quota": None},
    {"user": "ana", "active": False, "quota": 300},
]
print(dumps(users, indent=2)) # operación contraria al loads, de dict a JSON / el indent=2 te lo muestra vertical al ejecutarlo
str_json = dumps(users) #--> se puede guardar en una variable
print(type(str_json), str_json) 

