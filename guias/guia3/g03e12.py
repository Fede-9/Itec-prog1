#(12 de la 2)  Pedir nombres y sexo de personas y mostrar al final el total de mujeres y el 
# nombre de cada una.

preg1 = int(input("cuantas personas quiere registrar? "))
nombre = []
sexo = []
mujeres = []
total = 0


for i in range (preg1):
    dato1 = input("escriba su nombre: ")
    nombre.append(dato1)
    dato2 = input("escriba su sexo 'femenino' o 'masculino': ")
    sexo.append(dato2)


for x in range(len(sexo)):
    if sexo[x] == 'femenino':
        mujeres.append(nombre[x])
        total += 1
        
print("total de mujeres: ",total)
print("nombre de la o las mujeres ingresadas: ",mujeres)

# #OTRA FORMA DE HACERLO

preg1 = int(input("cuantas personas quiere registrar? "))
nombre = []
sexo = []
mujeres = []
total = 0


for i in range (preg1):
    dato1 = input("escriba su nombre: ")
    nombre.append(dato1)
    dato2 = input("escriba su sexo 'femenino' o 'masculino': ")
    sexo.append(dato2)
    if dato2=='femenino':
        mujeres.append(dato1)
        total+=1

print(mujeres)
print(total)


#LISTA POR COMPRENSION

n = ['fede','ana','juan','sonia']
s = ['masculino','femenino','masculino','femenino']
c = 0

nom = [n[i] for i in range(len(n)) if s[i]=='femenino']
print(nom)