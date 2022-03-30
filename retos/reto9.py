#Listar los números pares del 10 al 20.

pares=[]
for i in range(10,21):
    if i % 2 == 0:
        pares.append(i)

print(pares)
