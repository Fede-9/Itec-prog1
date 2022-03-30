#12. Mostrar el valor doble del número de dos cifras (que es el único número) encontrado en la cadena.
 #Ej.: 'Juan tiene 25 años' mostraría el número 50, 
 # ‘El dólar va a llegar este mes a 57 pesos casi seguro’,  mostraría 114.

cadena = 'Fede tiene 100 pesos'
cadena1 = cadena.split()
valor = (int(cadena1[2]) * 2)   #convierto el valor de la lista en un entero
doble = f'Fede tiene {valor} pesos'
print(doble)

#OTRA FORMA DE HACERLO

frase = input('Ingrese su frase con numero: ')
fraseSplit = frase.split()
doble = 0


for i in range(len(fraseSplit)):
    aux = ord(fraseSplit[i][0])
    if aux >= 48 and aux <= 57:
        tonumber = int(fraseSplit[i])
        doble = tonumber * 2

print('El numero que se encontro en el array es', tonumber)
print('El doble de ese numero es:',doble)