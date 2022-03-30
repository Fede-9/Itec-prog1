from datetime import datetime, date
def emailVal (correo):  #Validar correo electronico
    error = 'El correo ingresado no es válido.'
    validado = False
    while not validado: 
        dir = input(correo)
        try:
            if '@' and '.' in dir:
                aux  = dir.split('@')    
                usu = aux[0]
                resto = aux[1]
                aux2= resto.split('.')
                dominio = aux2[0]
                terminacion = aux[1]
                if ' ' or '' not in usu:    
                    if (dominio.isalpha() == True) and (terminacion!=''):
                        validado=True
                        print('Direccion de correo valida.')
                    else:
                        print(f'{error}')            
                else:
                    print(f'{error}')            
            else:
                print(f'{error}')            
        except: 
            print(f'{error}')
def fecVal(mensaje):  #Validar fecha con el import Datetime(datetime)
    error = '*Sonido de error* La fecha ingresada no es valida.'
    validado = False 
    while not validado:
        fecha= input(mensaje)
        try:
            fec = datetime.strptime(fecha, '%d/%m/%Y') #pasar a formato dia mes año
            print('Fecha valida.')
            validado = True
        except :
            print(f'{error}')
    return fecha
def edad(mensaje): #Calcular edad con el import date (datetime)
    validado = False
    while not validado:
        fn = input(mensaje)
        try:
            hoy = date.today()
            dn, mn, an = fn.split('-')
            dn = int(dn)
            mn = int(mn)
            an = int(an)
            dh = hoy.day
            mh = hoy.month
            ah = hoy.year
            e = ah - an
            if (mn > mh) or (mn == mh and dn > dh):
                e -= 1
                validado = True
            else:
                print('Error. Fecha invalida.')
        except:
            print('Error. Fecha invalida.')
    return e

def inputInt(mensaje): #Inputint, valida que se ingrese un numero entero
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = int(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número entero")
    return numero
def inputFloat(mensaje): #input float, valida que se ingrese un decimal
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = float(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número real")
    return numero


def subrayar (): #Funcion super importante.
    print('_____________________________________________')
def backTomenu ():
    volver = True
    while volver: 
        op = input('>> Presione Enter para volver al Menu Principal:  ')
        if op == '': 
            volver = False
        else: 
            print('Debe presionar Enter para volver al Menu Principal.')



def todaysDate(): #fecha de hoy
    h = date.today()
    return h
def makeMenu(**kwargs):
    lista = []
    lista.append(kwargs)
    c = 1
    for e in lista: 
        for valor in e.values():
            salida = str(c)+ '> ' + valor
            print(salida)
            c += 1
import sys
infinite = 1e309
def valInt (mensaje, min=-infinite, max=infinite): #validar rango de enteros
    validado = False
    while not validado: 
        num= input(mensaje)
        try:
            num= int(num)
            if num > min and num < max:
                validado = True
            else: 
                print('Error. Debe respetar el rango.')
        except:
            print('Error. Debe ingresar un numero Entero.')
    return num
def valFloat (mensaje, min=-infinite, max=infinite):#validar rango de float
    validado = False
    while not validado: 
        num= input(mensaje)
        try:
            num= float(num)
            if num > min and num < max:
                validado = True
            else: 
                print('Error. Debe respetar el rango.')
        except:
            print('Error. Debe ingresar un numero Decimal.')
    return num