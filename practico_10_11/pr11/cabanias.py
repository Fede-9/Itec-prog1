# Faltaria agg manejo con fechas. Que se actualice en caso de que se cumpla la fecha cuando una pasajero sale de la cabaña

from os import system
from datetime import datetime

from input_string import inputString
from validacion_entero import validacionEntero 



def getCabins(file):

    """ Consigue los datos de las cabañas """
    cabins = []    
    try: # intenta abrir el archivo
        with open(file, 'r') as f:
            pass
    except: # si no existe el archivo, lo aclara
        return 'No cabins file founded'
    else:
        with open(file) as f:
            lines = f.readlines()
            for line in lines[1:]: # obtenemos todos los datos menos los titulos
                aux = line.strip() # sacamos los espacios y los saltos de linea
                if 'si' in aux: # si el valor si esta en aux que corresponde a una cabaña, significa que esta ocupada, por lo que podemos asignarle una fecha
                    aux = aux.split(',')
                    cabins.append({
                        'cabinNumber': aux[0],
                        'availablePeople':aux[1],
                        'price': aux[2],
                        'reserved': aux[3],
                        'inDate':aux[4],
                        'outDate':aux[5]
                    })
                else: # si no esta reservada, no le asignamos fecha
                    aux = aux.split(',')
                    cabins.append({
                        'cabinNumber': aux[0],
                        'availablePeople':aux[1],
                        'price': aux[2],
                        'reserved': aux[3],
                        'inDate':None,
                        'outDate':None
                    })
    return cabins

def printCabins(cabins):
    for cabin in cabins:
        for k,v in cabin.items():
            if k == 'cabinNumber':
                print(f'Numero de cabania: {v}')
            elif k == 'availablePeople':
                print(f'Cantidad de pasajeros permitidos: {v}')
            elif k == 'price':
                print(f'Precio de la cabaña: {v}')
            elif k == 'reserved':
                print(f'Reservada: {v}')
            elif k == 'inDate' and v != None:
                print(f'Fecha entrada: {v}')
            elif k == 'outDate' and v != None:
                print(f'Fecha salida: {v}')
        print('\n')    
    
                                
def printDic(dict):
    """ Printea key y values de un diccionario"""
    for k,v in dict.items():
        print(f'{k}. {v}')
    pass

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

def filterByPassengers(dict):
    """ Filtra las cabañas por cantidad de pasajeros especificados por la persona"""
    passengers = validacionEntero('Con cuantas personas va a alojarse?: ', max=4)          
    cabinsFiltered = [cabin for cabin in dict if int(cabin['availablePeople']) == passengers] 
    print(f'\nCabañas para {passengers} pasajeros\n')
    printCabins(cabinsFiltered)

def filterByPrice(dict):
    """ Filtra las cabañas por un maximo de precio establecido por el usuario"""
    budget = validacionEntero('Precio dispuesto a pagar: ')
    cabinsFiltered = [cabin for cabin in dict if int(cabin['price'][1:]) <= budget]
    if len(cabinsFiltered) > 1: 
        print(f'Cabañas por ${budget} o menos')
        printCabins(cabinsFiltered)
    else:
        print(f'No se encontraron cabañas por {budget} pesos o menos')
    
def filterByAvailability(dict):
    """ Filtra las cabañas que estan disponibles el dia de la fecha"""
    cabinsFiltered = [cabin for cabin in dict if cabin['reserved'] == 'no']
    if len(cabinsFiltered) > 1:
        print('Cabañas disponibles: \n')
        printCabins(cabinsFiltered)
    else:
        print('No se encuentran cabañas disponibles')
    
def menu():
    cabañas = getCabins('cabins.csv')
    opc_menu = {}
    opc_user = '' # opcion del usuario
    opc_menu['1'] = 'Mostrar todas las cabañas'
    opc_menu['2'] = 'Consultar disponibles por cantidad de pasajeros'
    opc_menu['3'] = 'Consultar por rango de precios'
    opc_menu['4'] = 'Consultar por todas las disponibles'
    opc_menu['5'] = 'Salir'
    mensaje = 'Desea elegir otra opcion? (s/n): '
    sigue = True
    while sigue:
        system('cls')
        printDic(opc_menu)
        opc_user = validacionEntero('Ingrese una opcion: ',max=len(opc_menu.keys()))
        if opc_user == 1:
            system('cls')
            printCabins(cabañas)
            sigue = seguir(mensaje)
            if sigue:
                #printDic(opc_menu)
                pass
        if opc_user == 2:
            system('cls')
            filterByPassengers(cabañas)
            sigue = seguir(mensaje)
            if sigue:
                printDic(opc_menu)
        if opc_user == 3:
            system('cls')
            filterByPrice(cabañas)
            sigue = seguir(mensaje)
            if sigue:
                printDic(opc_menu)            
        if opc_user == 4:
            system('cls')
            filterByAvailability(cabañas)
            sigue = seguir(mensaje)
            if sigue:
                printDic(opc_menu)   
        if opc_user == 5:
            sigue = False
            system('cls')
            print('Fin del programa')
        
        
        
        
def main():
    menu()
    

if __name__ == '__main__':
    main()