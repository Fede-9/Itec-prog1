## Funciones


# Crear nuestras propias funciones

def mi_funcion():
    """
    Esta funcion muestra en pantalla el string 'Rosario'
    """
    print('Rosario')

mi_funcion()
help(mi_funcion)   #esto me muestra la aclaracion que esta entre comillas.




print('--------------------------------------')
print('---------FUNCIONES CON PARAMETROS y ARGUMENTOS-----------')

def mi_funcion_2(nombre): # Cuando definimos la funcion se llama PARAMETROS
    
    print(nombre) # print('Escalera')

mi_funcion_2(nombre = 'Escalera') # Llamamos a la funcion y le especificamos UN ARGUMENTO
mi_funcion_2(nombre = 'Paris')
mi_funcion_2(nombre = 500)

print('--------------------------------------')
print('---------FUNCIONES CON PARAMETROS y ARGUMENTOS --2----------')

def suma_1000(numero):
    
    print(numero + 1000) # print(10 + 1000)

suma_1000(numero = 10) # ---> Muestra en pantalla 1010
suma_1000(numero = 2000) # ---> Muestra en pantalla 3000



print('--------------------------------------')
print('---------FUNCIONES CON PARAMETROS y ARGUMENTOS --3----------')

# Argumentos por default

def mi_funcion_3(numero = 0, nombre = 'Sin nombre'):
  
    print('El numero es:',numero , 'Y Pertenece a la persona:', nombre)

# mi_funcion_3(numero=500, nombre='fernando')
mi_funcion_3()
mi_funcion_3(numero=1000, nombre='Fernanda')