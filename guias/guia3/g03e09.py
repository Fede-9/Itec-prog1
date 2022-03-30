#Cargar en dos listas paralelas nombres y sueldos. Luego mostrar los nombres de las 
# personas que ganan más de $85000.

preg1 = input("desea cargar su nombre y sueldo? ")
nombres = []
sueldos = []
ganan_mas = []

while preg1 == 'si':
    dato1 = input("escriba su nombre: ")
    nombres.append(dato1)
    dato2 = int(input("escriba el monto de sueldo: "))
    sueldos.append(dato2)
    preg1 = input("hay mas personas para cargar? ")
    
for i in range(len(nombres)):
    if sueldos[i] > 85000:
        ganan_mas.append(nombres[i])


print("nombre de los empleados que ganan mas de 85000 pesos: ", ganan_mas)


#OTRA FORMA DE HACERLO



preg1 = int(input('cuantas personas desea registrar? '))
nombres = []
sueldos = []
ganan_mas = []

for i in range(preg1):
    dato1 = input('ingrese el nombre: ')
    nombres.append(dato1)
    dato2 = int(input('ingrese su sueldo: '))
    sueldos.append(dato2)
    
    
for x in range(len(nombres)):
    if sueldos[x] > 85000:
        ganan_mas.append(nombres[x])

print('nombre de los empleados que ganan mas de $85000: ',ganan_mas)



#lista por comprension

empleados = ['fede','nonito','maxi','papel']
sueldos = [90000,1555,100000,23]
sueldoMayor = [empleados[x] for x in range(len(empleados)) if int(sueldos[x]>85000)]
print(sueldoMayor)