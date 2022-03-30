# Según la consigna del ejercicio 12 de la Guía 5, que dice:
# Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los
#  nombres de los mayores de edad.
# Funciones de carga y cálculo de edad.

# Reformulen la solución utilizando almacenamiento en archivo de texto. Para ello:
# 1) Escriban un programa de carga, que tome los datos solicitados al usuario y los almacene en un 
# archivo de texto en el formato que prefieran. Pueden previamente almacenarlos en listas o no, es opcional.




nombres = ['Cometto, Federico', 'Lerda, Tomas', 'Lopez, Manuel', 'Saby, Lucas', 'Mora, Matias']
fechas = ['28/07/1998', '25/03/2010', '12/05/2003', '23/08/1997', '21/01/2020']

with open('data.txt', 'w') as f:  #Abre y cierra el archivo
    for x in range(len(nombres)):
        salida = nombres[x] + ' - ' + fechas[x] +  '\n'
        f.write(salida)
