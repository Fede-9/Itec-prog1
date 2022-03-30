#Ingresar la lluvia caída en milímetros para cada día de la semana.
 #Mostrar al final el total de lluvia caída y la cantidad de días que no llovió.

print("INGRESAR EN MILIMETROS LA CANTIDAD DE LLUVIA DURANTE LOS DIAS DE LA SEMANA !!")
total = 0
no_llovio = 0
lluvia = 7
for x in range(lluvia):
    x = int(input("ingrese la cantidad de lluvia: "))
    if x > 0:
        total += x
    elif x == 0:
        no_llovio += 1
print("cantidad de lluvia durante la semana: ", total, "milimetros")
print("dias que no llovio: ", no_llovio)

