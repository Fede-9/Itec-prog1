#Pedir los montos de sueldos de los empleados de una empresa hasta que no haya más y mostrar el total.
contador = 0
empleados = int(input("Cuantos sueldos van a registrar?: "))
for x in range(empleados):
    monto = int(input("Cual es el monto de su sueldo ?: "))
    contador += monto 

print("Total :", contador)