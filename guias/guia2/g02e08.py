#Ingresar autos y sus precios y contar cuantos valen entre $1.460.000 y $2.850.000. 
# Terminar la carga cuando el valor ingresado sea $0.

auto = int(input("cuantos autos desea ingresar? "))
contador = 0
x = 0
while auto != x:
    valor = int(input("cual es el valor de su auto? "))
    x += 1
    if valor > 1460000 and valor < 2850000:
        contador += 1
    
print("los autos con valor entre 1460000 y 2580000 pesos son: ", contador)

#DOS FORMAS DE HACERLO

auto = int(input("cuantos autos desea ingresar: "))
cont = 0

for i in range(auto):
    dato1 = int(input("cual es el valor de su auto: "))
    if dato1 > 1460000 and dato1 < 2850000:
        cont += 1

print(cont)
