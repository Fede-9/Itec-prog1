#Crear una función que calcule el Índice de Masa Corporal

def imc(peso,altura):
    peso = int(input('Ingrese su peso: '))
    altura = float(input('Ingrese su altura: '))
    calculo = peso//pow(altura,2)
    return calculo

print(f'IMC de la persona: {imc(peso=int, altura=float)}')
