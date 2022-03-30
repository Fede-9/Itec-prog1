# 7. Almacenar en dos  listas paralelas, nombres y sexos de 8 personas.
#  Al finalizar, recorrerlas y mostrar los nombres de las mujeres. Dos funciones: carga y mostrarMujeres

names = []
sex = [] 

def carga(cantidad):
    for i in range(cantidad):
        n = input(f'Ingrese el nombre de la persona {i+1}: ')
        names.append(n)
        s = input(f'Ingrese el sexo de la persona {i+1} (m/f): ')
        sex.append(s)

def mostrarMujeres(nombres, sexo):
    aux = []
    for i in range(len(nombres)):
        if sexo[i] == 'f':
            aux.append(nombres[i])
    return aux


carga(8)

mujeres = mostrarMujeres(names,sex)

print('Nombres de las mujeres:', mujeres)

