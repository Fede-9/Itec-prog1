loteria = [3,2,5,7,10,20,30]

def app(lista):
    
    with open('numeros_pares.txt','w') as archivo: # Si no existe, numeros_pares.txt, entonces lo creara
        archivo.write('La lista de numeros pares es: \n')
        for numero in lista:
            if numero % 2 == 0:
                archivo.write(str(numero) + '\n')


app(loteria)