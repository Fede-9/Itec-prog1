# Metodos utiles de aplicacion para Listas
print('------ APPPEND -------')

loteria = [10, 20, 30, 40, 50]
colores = ['azul','rojo','verde','amarillo']

# Append

loteria.append(90)
loteria.append('EcaCapacitaciones')
print(loteria)

# Count

print('-------- COUNT-----------')
elementos = [10, 20, 10, 10, 30, 20, 10]

cantidad_de_10 = elementos.count(10) # cantidad_de_10 = 4
print(cantidad_de_10)

# Insert

print('-------- INSERT -----------')

print(loteria)

# loteria[0] --> 10
# loteria[1] --> 20
# loteria[2] --> 25
# loteria[3] --> 30

loteria.insert(2 , 25)
print(loteria)