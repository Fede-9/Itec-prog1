# Instruccion BREAK : nos permite salir de un ciclo while.

numero = 0

while True:
    numero += 1 
    print('El valor de la variable numero es:', numero)
    if numero == 5: # 1 == 5 ---> False
        break


print('El valor FINAL de la variable numero es:', numero)


# 1era Ejecucion del WHILE: numero = 1 --- 1 == 5 ----> FALSE --> no entra dentro de la clausula IF
# 2nda Ejecucion del While: numero = 2 --- 2 == 5 ----> FALSE --> no entra dentro de la clausula IF
# 3era Ejecucion del While: numero = 3 --- 3 == 5 ----> FALSE --> no entra dentro de la clausula IF
# 2nda Ejecucion del While: numero = 4 --- 4 == 5 ----> FALSE --> no entra dentro de la clausula IF
# 2nda Ejecucion del While: numero = 5 --- 5 == 5 ----> TRUE  -->  SI entra dentro de la clausula IF