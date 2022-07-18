#2- Pedir tres notas, calcular el promedio y mostrarlo.

nota1 = int(input("digame su primer nota: "))
nota2 = int(input("digame su segunda nota: "))
nota3 = int(input("digame su tercer nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f'Promedio: {promedio}')


suma = 0
cont = 0
for i in range(3):
    nota = int(input('ingrese nota: '))
    suma += nota
    cont += 1

print('Promedio: ',suma/cont)