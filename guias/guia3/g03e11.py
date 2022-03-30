#Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo 
# y mostrar los nombres de los mayores de edad.

preg1 = int(input("cuantas personas quiere registrar? "))

nombres = []
años = []
meses = []
dias = []
mayores = []


for i in range (preg1):
    dato1 = input("ingrese su nombre: ")
    nombres.append(dato1)
    dato2 = int(input("ingrese el año de su nacimineto: "))
    años.append(dato2)
    dato3 = int(input("ingrese el mes de su nacimiento: "))
    meses.append(dato3)
    dato4 = int(input("ingrese el dia de su nacimiento: "))
    dias.append(dato4)


for x in range (preg1):
    if (años[x] < 2003):
        mayores.append(nombres[x])
    elif años[x] == 2003:
        if meses[x] < 5:
            mayores.append(nombres[x])
        elif meses[x] == 5:
            if dias[x] <= 7:
                mayores.append(nombres[x])

print("Las personas mayores de edad son: ", mayores)
            

