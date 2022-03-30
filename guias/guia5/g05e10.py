# 10. Cargar una lista con números. Invertir los elementos (sin usar reverse). Mostrar.

def invertirLista(lista):
    aux = []
    for i in range(len(lista),0,-1):
        aux.append(i)
    return aux

numbers = [1,2,3,4,5,6,7,8,9,10]
#print(numbers[::-1])
num_invertidos = invertirLista(numbers)
print(num_invertidos)