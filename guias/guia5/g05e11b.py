# 11. Ingresar la lluvia caída en milímetros para cada día de la semana.
#  Mostrar al final el total de lluvia caída y el nombre del día que más llovió.


dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']

def clima(dias):
    total = 0
    aux = 0
    mas_llovio = ' '
    for i in dias:
        lluvia = int(input(f'Ingrese lluvia del dia {i}: '))
        total += lluvia
        if lluvia > aux:
            aux = lluvia
            mas_llovio = i

    return mas_llovio , total


mas_llovio, total = clima(dias)

print(f'Total lluvia: {total}')
print(f'Dia que mas llovio: {mas_llovio}')