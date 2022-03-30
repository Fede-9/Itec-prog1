#Guardar en una lista los números pares mayores que 0 y menores que 31. 

preg1 = input("desea ingresar un numero? ")
numeros = []

while preg1 == 'si':
    preg2 = int(input("ingrese un numero: "))
    if preg2 > 0 and preg2 < 31 and preg2%2 == 0:
        numeros.append(preg2)

    preg1 = input("desea ingresar otro numero? ")
    
print("el o los numeros pares ingresados son: ", numeros)


#OTRA FORMA DE HACERLO


usuario = int(input('cuantos numeros desea ingresar? '))
num = []

for i in range(usuario):
    dato1 = int(input('ingrese un numero: '))
    if dato1 > 0 and dato1 < 31 and dato1%2 == 0:
        num.append(dato1)

print(num)


# lista por comprension

numeros = [2,23,25,44,63,12,15,13]
selec = [num for num in numeros if num%2==0 and num>0 and num<31]
print(selec)