#Pedir nombres y sexo de personas y mostrar el total de mujeres y el nombre de cada una.

total = int(input("cuantas persona desea registrar? "))
nombre1 = []
x = 0
cont = 0
femenino = 1
while total != x:
    nombre2 = input("digame su nombre: ")
    sexo = input("cual es su sexo? ")
    x += 1
    if sexo == 'femenino':
        cont += 1
        nombre1.append(nombre2)
    
print("total de mujeres: ", cont)
print("nombre de cada una: " , nombre1)

#DOS FORMAS DE HACERLO

total = int(input("cuantas personas quiere registrar? "))

nombre1 = []
cont = 0

for i in range(total):
    nombre2 = input('ingrese su nombre: ')
    sexo = input('cual es su sexo: ')
    if sexo == 'femenino':
        cont += 1
        nombre1.append(nombre2)

print('total de mujeres: ',cont)
print('nombres/s: ',nombre1)
