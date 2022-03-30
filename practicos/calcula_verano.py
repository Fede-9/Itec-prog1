
def verano(fecha):  # aaaa-mm-dd
    retorno = 0
    
    a, m, d = [int(e) for e in fecha.split('-')]  # esto es una lista por comprencion / MIRAR COMO FUNCIONA EN LA CARPETA DE CLASES VIRTUALES

    if (m == 12 and d >= 21):
        retorno = a + 1   # retorna el año ingresado mas 1 año
    elif (m == 1) or (m == 2) or (m == 3 and d <= 20):
        retorno = a # retorna el mismo año ingresado
    else:
        retorno = -1    # retorna -1 me sirve como indicador de que no nacio en verano
    return retorno 

print(verano('1998-12-30'))
print(verano('1998-01-23'))
print(verano('1998-07-28'))