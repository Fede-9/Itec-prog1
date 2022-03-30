#Procesos para las salidas:
#1) Mostrar las iniciales de los nombres con apellido completo de todas las personas.
#2) Decir cual es el nombre de pila más largo.
#3) Mostrar el promedio de edad de las mujeres. (Pueden usar la función edad del módulo calcula_edad que está subida en el Classroom)

nom = ['Torres, Ana','Hudson, Kate','Quesada, Benicio','Campoamores, Susana','Santamaria, Carlos','Skarsgard, Azul','Catalejos, Walter'] 

#EJERCICIO 1:
nom2 = []
apell = []

for i in range(len(nom)):
    nom1 = nom[i].find(',')
    nom2.append(nom[i] [nom1 + 2 : ])
    apell.append(nom[i][ : nom1])
print('Iniciales y apellidos de las personas:')
for x in range(len(nom2)):
    nuevos_nombres = nom2[x][0] + '. ' + apell[x]
    print(nuevos_nombres)

#EJERCICIO 2:

contador_letras = 0
nombre_mas_largo = ''

for z in range(len(nom2)):
    if len(nom2[z]) > contador_letras:
        contador_letras = len(nom2[z])
        nombre_mas_largo = nom2[z]
        
print (f'El nombre mas largo es: {nombre_mas_largo}')

    
#EJERCICIO 3:

fechas_nacimiento = ['02/05/1943', '07/09/1984', '10/02/1971', '21/12/1967', '30/01/1982', '30/08/1995', '18/07/1959']
sexo_persona = ['f', 'f','m', 'f', 'm', 'f','m']

from calcula_edad import edad
mujeres = 0
fechas_mujeres = 0

for w in range(len(sexo_persona)):
    if sexo_persona[w] == 'f':
        fechas_mujeres += edad(fechas_nacimiento[w])
        mujeres += 1

print(f'El promedio de edad de las mujeres es de {fechas_mujeres // mujeres} años')