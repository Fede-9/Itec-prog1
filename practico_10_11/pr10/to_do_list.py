import sys
import os
from os import remove, system
from datetime import datetime

from validacion_entero import validacionEntero
from input_string import inputString


def addCategory(category):
    """ agrega una categoria mas a la lista de archivos """
    try:
       with open(f'{category}.csv','r') as f:
            return 'Categoria existente'
    except: 
        with open(f'{category}.csv','w') as f:
          f.write('tarea,categoria,fecha\n')

def getCategories(): 
    """ A partir de los archivos csv creados, obtiene las categorias de las tareas """
    categories = os.listdir('.')
    categories = list(filter(lambda x: ('.csv' in x) and ('demoradas' not in x), categories)) # consigo el nombre de los archivos
    categories = list(map(lambda x: x[0:-4], categories)) # obtengo el nombre de los archivos sin csv, para usarlos para representar categorias
    return categories

def addTask():
    """ Agrega tarea al archivo de categoria correspondiente"""
    categories = getCategories()
    choosenCategory = ''
    task = {}
    if len(categories) >= 1:
        print('-- CATEGORIAS DISPONIBLES --')
        for category in categories:
            print(f'{category.title()}')
        while choosenCategory.lower() not in categories:
            choosenCategory = input('A que categoria corresponde su tarea?: ')
        if choosenCategory.lower() not in categories:
            system('cls')
            print('La categoria no existe, intente nuevamente')
        else:
            system('cls')
            print('-- AGREGANDO CATEGORIA --')
            task['tarea'] = inputString('Descripcion de la tarea: ')
            task['categoria'] = choosenCategory
            task['fecha'] = validarFecha() # fecha formato datetime con hora incluida
            task['diasRestantes'] = (task['fecha'] - datetime.today()).days
            task['fecha'] = task['fecha'].strftime('%d-%m-%Y %H:%M') # le doy el formato correcto a la fecha 
            with open(f'{choosenCategory}.csv','a') as f:
                for k,v in task.items():
                    if k == 'diasRestantes': # si la key es fecha, no le agrego coma, ya que es la ultima
                        f.write(f'{v}\n')
                    else:
                        f.write(f'{v},')
        return task
    else:
        return 'NO EXISTEN CATEGORIAS, VUELVA AL MENU PARA AGREGAR ALGUNA'

def getTasks(file):
    """" Obtiene las tareas del archivo especificado """
    tasks = []
    final = []

    with open(file) as f:
            content = f.readlines() # lista con valores csv
            for i in range(1,len(content)):
                tasks.append(content[i].strip())
            for e in tasks:
                aux = e.split(',')
                final.append({
                    'tarea' : aux[0],
                    'categoria': aux[1],
                    'fecha': aux[2],
                    'diasRestantes': aux[3]
                })

    if len(final) >= 1:
        return final
    else:
        return []
    
def getAllTasks():
    """ Obtiene todas las tareas de todas las categorias """
    categories = getCategories()
    allTasks = []
    try:
        for category in categories:
            aux = getTasks(f'{category}.csv')
            allTasks += aux
        return sorted(allTasks,key=lambda x: x['diasRestantes'],reverse=True)
    except:
        return []
    
    


def moveTasks(file,task):
    """ Pasa tareas a otro archivo"""
    try:
        with open(file) as f:
            pass
    except:
        with open('demoradas.csv', 'w') as f:
            f.write('tarea,categoria,fecha\n')
            for k,v in task.items():
                if k == 'fecha':
                    f.write(v)
                else:
                    f.write(f'{v},')
                        
    else:
        with open('demoradas.csv', 'a') as f:
            f.write('\n')
            for k,v in task.items():
                if k == ['fecha']:
                    f.write(v)
                else:
                    f.write(f'{v},')  
        
        
def removeTask(file, task):
    """ Remueve una tarea de un archivo reescribiendolo, sin la tarea especificada"""
    with open(file) as f:
        lines = f.readlines()
    with open(file,'w') as f:
        for line in lines:
            if task not in line:
                f.write(line)
                 
def getDelayedTasks():
    """ Cheuquea si hay tareas demoradas, y si las hay, las printea."""
    file = 'demoradas.csv'
    delayedTasks = []
    final = []
    try:
        with open(file) as f:
            content = f.readlines()
            for i in range(1,len(content)):
                delayedTasks.append(content[i].strip())
            for e in delayedTasks:
                aux = e.split(',')
                final.append({
                    'tarea': aux[0],
                    'categoria': aux[1],
                    'fecha': aux[2]
                })
    except:
        return 'No existen tareas demoradas'
    else:
        for i in range(len(final)):
            print(f'{i} - TAREA: {final[i]["tarea"]}')
            print(f'CATEGORIA: {final[i]["categoria"]}')
            print(f'Fecha: {final[i]["fecha"]}\n')
      
def chooseTask():
    """ Obtiene todas las tareas, y a partir de su indice en la lista, devuelve la elegida por el usuario"""
    tasks = getAllTasks()
    print(len(tasks))
    if len(tasks) >= 1:
        printTasks()
        choosenTask = validacionEntero('Ingrese el numero correspondiente a la tarea: ',max = len(tasks) - 1)
        return tasks[choosenTask]
    else:
        return []
           

def printTasks():
    """ Printea todas las tareas con sus categorias y tiempo restante"""
    tasks = getAllTasks()
    if len(tasks) < 1:
        system('cls')
        print('Sin tareas para mostrar')
        return []
    else:
        print(' -- ATENCION, SI YA PASO EL PLAZO DE ALGUNA TAREA SERA PASADA AL ARCHIVO "DEMORADAS.CSV" AUTOMATICAMENTE --')
        sigue = seguir('Desea continuar?(s/n): ')
        if sigue:
            system('cls')
            for i in range(len(tasks)):
                daysRemaining = int(tasks[i]['diasRestantes'])
                if daysRemaining < 0:
                    category = tasks[i]['categoria']
                    task = tasks[i]['tarea'].lower()
                    tasks[i].pop('diasRestantes')
                    moveTasks('demoradas.csv',tasks[i])
                    removeTask(f'{category}.csv',task)
                    print(tasks[i])
                else:
                    print('')
                    print(f'{i} - TAREA: {tasks[i]["tarea"]}')
                    print(f'CATEGORIA: {tasks[i]["categoria"]}')
                    print(f'Tiempo restante: {tasks[i]["diasRestantes"]} dias\n')

        

def checkTodayTasks():
    tasks = getAllTasks()
    today = datetime.today()
    tasks = [t for t in tasks if t['diasRestantes'] == '0']
    if len(tasks) >= 1:
        for i in range(len(tasks)):
            print('-- TAREAS DENTRO DE LAS 24 HORAS --')
            print(f'{i} - TAREA: {tasks[i]["tarea"]}')
            print(f'{i} - CATEGORIA: {tasks[i]["categoria"]}')
            print(f'{i} - FECHA: {datetime.strptime(tasks[i]["fecha"],"%d-%m-%Y %H:%M")}')
            sigue = seguir('Desea marcar alguna como completada? (s/n): ')
            if sigue:
                choosenTask = validacionEntero('Ingrese el numero correspondiente a la tarea segun el menu anterior: ',max = len(tasks) - 1)
                removeTask(f'{tasks[0]["categoria"]}.csv',tasks[0]['tarea'])
        return tasks
    else:
        system('cls')
        print('No hay tareas para hoy')

        

def seguir(message):
    """ Funcion para determinar si sigue realizando acciones"""
    sigue = ''
    val = False
    while val == False:
        try:
            sigue = input(message)
            if sigue.lower() == 's':
                val = True
            elif sigue.lower() == 'n':
                return val
            else:
                print('Valor invalido, intente nuevamente')
        except:
            print('Error en el input')
    return val

def validarFecha():
    """ Validar fecha especifico para este programa, chequea que la fecha sea mayor al dia de hoy"""
    val = False
    today = datetime.today()
    while val == False:
        try:
            fecha = input('Ingrese fecha a cumplir: ')
            fecha = datetime.strptime(fecha, '%d-%m-%Y %H:%M')
            if fecha < today:
                system('cls')
                print('Fecha anterior al dia de hoy, intente nuevamente')
            else:
                val = True
        except:
            print('El formato no coincide con dd-mm-aaaa hh:mm')     
    return fecha



def printMenu(opciones):
    for k,v in opciones.items():
        print(f'{k}. {v}')
            
def menu():
    """ Menu interactivo to_do_list"""
    sigue = True
    message = 'Desea realizar otra accion? (s/n): '
    opcUser = '' # opcion usuario
    opcMenu = {}
    opcMenu['1'] = 'Agregar categoria/s'
    opcMenu['2'] = 'Agregar TAREA'
    opcMenu['3'] = 'Ver tareas para hoy'
    opcMenu['4'] = 'Ver tareas'
    opcMenu['5'] = 'Ver tareas demoradas'
    opcMenu['6'] = 'Remover tarea'
    opcMenu['7'] = 'Salir'
    while sigue:
            system('cls')
            printMenu(opcMenu)
            opc_user = validacionEntero('Ingrese su opcion: ', max=len(opcMenu.keys()))
            if opc_user == 1:
                cant = validacionEntero('Cuantas categorias desea agregar: ', max = 10)
                for i in range(cant):
                    system('cls')
                    categoria = inputString(f'Ingrese la categoria numero {i + 1}: ')
                    addCategory(categoria)
                sigue = seguir(message)
                if sigue:
                    printMenu(opcMenu)
            elif opc_user == 2:
                system('cls')
                print(addTask())
                sigue = seguir(message)
                if sigue:
                    printMenu(opcMenu)
            elif opc_user == 3:
                system('cls')
                checkTodayTasks()
                sigue = seguir(message)
                if sigue: 
                    printMenu(opcMenu)
            elif opc_user == 4:
                printTasks()
                sigue = seguir(message)
                if sigue: 
                    printMenu(opcMenu)
            elif opc_user == 5:
                system('cls')
                getDelayedTasks()
                sigue = seguir(message)
                if sigue:
                    printMenu(opcMenu)
            elif opc_user == 6: 
                task = chooseTask()
                if len(task) > 1:
                    archivo = f'{task["categoria"]}.csv'
                    tarea = task["tarea"].lower()
                    removeTask(archivo, tarea)
                else:
                    system('cls')
                    print('Sin tarea para remover')
                sigue = seguir(message)
                if sigue:
                    printMenu(opcMenu)
            elif opc_user == 7:
                sigue = False
    
    print('Fin del programa')
    

                                    


def main():
    menu()
    
    





    

if __name__ == '__main__':
    main()
    