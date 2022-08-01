#Decir cuántas veces se repite una letra cualquiera, en un texto dado. Por recorrido.

cadena = "Vivir solo cuesta vida"
cont = 0

for i in range(len(cadena)):
    if cadena[i] == "i":
        cont += 1

print("La cantidad de letras 'i' es de: ",cont) 


acum = 0
for x in cadena:
    if x == 'o':
        acum += 1

print(f'Cantidad de letras: {acum}')