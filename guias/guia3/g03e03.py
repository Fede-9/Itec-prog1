#Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
# Recorrerlas y guardar los nombres de las mujeres en una nueva lista. 
#Mostrar los elementos de la lista resultante.

lista1 = []
lista2 = []
lista3 = []

for x in range(1,9):
    preg1 = input(f"{x} - Escriba su nombre: ")
    lista1.append(preg1)
    preg2 = input(f"{x} - Escriba su sexo: ")
    lista2.append(preg2)
    if preg2 == 'femenino':
        lista3.append(preg1)

print("nombres ingresados: ", lista1)
print("sexo de las personas registradas: ", lista2)
print("nombre de las mujeres: ", lista3)

#DOS FORMAS DE HACERLO

nombres = ['fede','ana','lucas','lucia']
sexos = ['masculino','femenino','masculino','femenino']
nombre_mujer = []

for i in range(len(sexos)):
    if sexos[i] == 'femenino':
        nombre_mujer.append(nombres[i])

print('nombre de ls mujeres: ',nombre_mujer)
