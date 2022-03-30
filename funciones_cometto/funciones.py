import sys
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


def inputInt(mensaje): #validar entero
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = int(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número entero")
    return numero

def inputFloat(mensaje): #validar flotante/decimal
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = float(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número real")
    return numero

def subrayar (): #Funcion subrayar
    print('_____________________________________________')

def backTomenu (): # funcion para menu
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

def inputRangeInt(mensaje, vi, vf):
    valido = False
    while not valido:
        numero = input(mensaje)
        try:
            numero = int(numero)
            if vi <= numero <= vf:
                valido = True
            else:
                print('El rango de valores es de', vi,'a', vf)
        except:
            print("Error. Debe ingresar un número entero")
    return numero

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


def inputString(msg,**condiciones): #validar largo de string
    strng = input(msg)
    cond = False
    try: 
        while cond == False:
            string_len = len(strng)
            if "max" in condiciones.keys() and "min" in condiciones.keys():
                max = condiciones["max"]
                min = condiciones["min"]
                if (string_len >= min) and (string_len <= max):
                    cond = True
                    return strng
                else:
                    print(f'El largo de la string tiene que ser mayor que {min} y menor que {max}')
                    strng = input(msg)
            elif 'max' in condiciones.keys() and 'min' not in condiciones.keys():
                max = condiciones['max']
                if string_len <= max:
                    cond = True
                    return strng
                else:
                    print(f'El largo de la string tiene que ser menor que {max}')
                    strng = input(msg)
            elif 'min' in condiciones.keys() and 'max' not in condiciones.keys():
                min = condiciones['min']
                print(min)
                if string_len >= min:
                    cond = True
                    return strng
                else:
                    print(f'El largo de la string tiene que ser mayor que {min}')
                    strng = input(msg)
            else:
                return strng
    except ValueError:
        print('Valor invalido')


# sirve para sumar N cantidad de numeros.
def suma(*args):  
    cont = 0
    for e in args:
        cont += e
    return cont

#Concatenar un número indeterminado de strings con un caracter determinado (por defecto un espacio)
def concatenar(*args, caracter=''):
    return caracter.join(args)

def inputNumber(tipo, mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            if tipo == "entero":
                numero = int(numero)
            elif tipo == "real":
                numero = float(numero)
            else:
                print("Check! entero o real. Ctrl C!")
            validado = True
        except:
            print("Error. Debe ingresar un número", tipo)
    return numero

def validacionEntero(message='Imgrese un numero entero: ', min=0,max=sys.maxsize):
    """" Recibe un mensaje, minimo y maximo para el ingreso de un entero"""
    validacion = False
    while validacion == False:
        try:  
            numero = inputNumber('entero',message)
            if numero >= min and numero <= max:
                validacion = True
                return numero
            else: 
                print(f'Numero entero mayor o igual {min} y menor o igual que {max}')
        except:
            return 'Error, argumento invalido'

def validacionFloat(message='Ingrese un numero: ', min=0, max=sys.maxsize):
    """" Recibe un mensaje, minimo y maximo para el ingreso de un entero"""
    validacion = False
    while validacion == False:
        try:  
            numero = inputNumber('real',message)
            if numero >= min and numero <= max:
                validacion = True
                return numero
            else: 
                print(f'Numero entero mayor o igual {min} y menor o igual que {max}')
        except:
            return 'Error, argumento invalido'




if __name__=='__main__': #para probar las funciones
    print(concatenar('como va?', 'buenas noches', 'hasta luego', 'hasta mañana'))
    print(concatenar('como va?', 'buenas noches', 'hasta luego', 'hasta mañana', caracter=' - '))
    print(concatenar('como va?', 'buenas noches', 'hasta luego', 'hasta mañana', caracter=' + '))
    print(suma(5,5,5))
    print(inputInt('ingrese numero: '))
    print(edad('28-07-1998'))
