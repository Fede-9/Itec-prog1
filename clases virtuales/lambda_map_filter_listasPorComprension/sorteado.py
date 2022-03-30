def cuadrado(x):
    return x*x

print(cuadrado(3))
print((lambda x: x*x)(3))  #es lo mismo que escribir def .....
# Lambda son funciones anonimas de una sola linea que se utlizan mucho en funcional
lista = [2,1,3]
print(list(map(cuadrado,lista)))
# la funcion map tiene dos parametros el primero que es una funcion y el segundo es un iterable y lo que hace
# es aplicar la funcion a cada elemto del iterable


# aca lo hago todo junto
print(list(map(lambda x: x*x, lista)))

# otra funcion que se utiliza mucho en funcional es fillter la diferencia con la funcion map es que 
# la salida tiene que tener valor de verdad es decir verdadero o falso
print(list(filter(lambda x: x%2==1, lista)))




#OTRO EJEMPLO

def stringuea(x):
    return str(x)


print(list(map(lambda x: str(x), lista)))
print(list(map(stringuea, lista)))