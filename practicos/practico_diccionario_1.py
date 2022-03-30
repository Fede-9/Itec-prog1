# Crear dos listas, una de mujeres y otra de varones, cuyos elementos sean diccionarios con 
# todos los datos de cada persona, a partir de las siguientes listas paralelas.
# Leer cuidadosamente la consigna!

names = ['Khan', 'Omar', 'Sara', 'Ali', 'Mohammed', 'Sofia', 'Mateo']
ages = [60, 50, 55, 70, 25, 20, 40]
heights = [1.75, 1.90, 1.55, 1.80, 1.65, 1.71, 1.88]
sexs = ['M', 'M', 'F', 'M', 'M', 'F', 'M']


varones = []
mujeres = []
for i in range(len(names)):
    if sexs[i] == 'M':
        varones.append({'names':names[i],'ages':ages[i],'heights':heights[i]})
    else:
        mujeres.append({'names':names[i],'ages':ages[i],'heights':heights[i]})
        

dicc = open('continuacion.txt', 'w') 
dicc.write(str(varones)+'\n') 
dicc.write(str(mujeres))
dicc.close()