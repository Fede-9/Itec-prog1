# 1.Escribir un programa que almacene las asignaturas de un curso
#(por ejemplo: Matemáticas, Física, Química, Historia y Lengua) en una lista
#y la muestre por pantalla el mensaje: Yo estudio <asignatura>
#donde <asignatura> es cada una de las asignaturas de la lista. 

asignaturas = ['matematicas','fisica','quimica','historia','lengua']
for i in asignaturas:
    print(f'yo estudio {i}')



# 2. Escribir un programa que almacene las asignaturas de un curso
#(por ejemplo: Matemáticas, Física, Química, Historia y Lengua) en una lista,
#pregunte al usuario la nota que ha sacado en cada asignatura,
#y después las muestre por pantalla con el mensaje:
#En <asignatura> has sacado <nota>
#donde <asignatura> es cada una de las asignaturas de la lista
#y <nota> cada una de las correspondientes notas introducidas por el usuario. 


asignaturas = ['matematicas','fisica','quimica','historia','lengua']
notas = []
for x in asignaturas:
    nota = int(input(f'ingrese su nota de {x} '))
    notas.append(nota)

for z in range(len(asignaturas)):
    print(f'En la asignatura {asignaturas[z]} su nota es {notas[z]} ')



# 3. Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 


numeros_ganadores = []

for i in range(6):
    numeros_ganadores.append(int(input('ingrese uno de los numeros ganadores: ')))
    numeros_ganadores.sort()

print(f'los numeros ganadores son: {numeros_ganadores}')



# 4. Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo: Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura y
# elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir. 


asignaturas = ['matematicas','fisica','quimica','historia','lengua']
asignaturas_aprobadas = []
repetir = []
for i in asignaturas:
    nota = float(int(input(f'ingrese su nota de la asignatura {i}: ')))
    if nota > 4:
        asignaturas_aprobadas.append(i)
    else:
        repetir.append(i)

print(f'Las asignaturas que debe repetir son: {repetir}')
print(asignaturas_aprobadas)
