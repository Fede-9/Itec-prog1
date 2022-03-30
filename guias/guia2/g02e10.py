#Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo y 
# mostrar el nombre de la persona que menos gana.

empleados = int(input("cuantos salarios quiere registrar? "))
nombre1 = []
salario1 = []
cont = 0
menos_gana = ''
  
for x in range (empleados):
    nombre2 = input("ingrese su nombre: ")
    nombre1.append(nombre2)
    salario2 = int(input("ingrese su sueldo: "))
    salario1.append(salario2)
    cont += salario2


for x in range(len(salario1)):
    if (salario1[x] < cont):
        cont = salario1[x]
        menos_gana = nombre1[x]


print("el que menos gana es ", menos_gana)
print("su sueldo es de: ", cont)