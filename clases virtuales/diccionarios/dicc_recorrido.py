gente = { 
    'Juan': 31,
    'Pedro': 23,
    'Luis': 44
}


for clave in gente.keys():
    print(clave)

for valor in gente.values():
    print(valor)

for clave, valor in gente.items():
    print(clave, '->', valor)
