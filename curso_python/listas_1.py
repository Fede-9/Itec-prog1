# Multiple Indexacion

lista_anidada = [ 1,2,3, [4,5,['anidado']]]
# lista_anidada[0] --> 1
# lista_anidada[1] --> 2
# lista_anidada[2] --> 3
# lista_anidada[3] --> [4,5,['anidado']]

# lista_anidada[3][0] --> 4
# lista_anidada[3][1] --> 5
# lista_anidada[3][2] --> ['anidado']

# lista_anidada[3][2][0] ---> 'anidado'

print(lista_anidada[3])
print(lista_anidada[3][2])
print(lista_anidada[3][2][0])