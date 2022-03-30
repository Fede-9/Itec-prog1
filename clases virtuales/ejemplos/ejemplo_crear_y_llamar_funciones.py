#Crear la funcion

def suma(a, b):  # parametros
    x = a + b
    print(x)

suma(5,4)  #Llamar a la funcion en donde 5 y 4 son los argumentos


#EJEMPLOS DE FUNCIONES: calculadora

def sumar(a,b): #Definimos la función sumar
    x = a + b
    print (("Resultado"), (x))
def restar(a,b):#Definimos la función restar
    x = a - b
    print (("Resultado"), (x))
def multiplicar(a,b):#Definimos la función multiplicar
    x = a * b
    print (("Resultado"), (x))
def dividir(a,b):#Definimos la función dividir
    x = a / b
    print (("Resultado"), (x))

#desde aca llamo ala funcion que quiero
x = int(input('numero: '))
z = int(input('otro numero: '))
restar(x,z)      #argumentos con datos ingresados por el usuario
restar(10,3)    #le puedo pasar los argumentos
