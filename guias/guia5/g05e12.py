#12. Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y
#mostrar los nombres de los mayores de edad. 
#Funciones de carga y cálculo de edad.


from calcula_edad import edad

def carga():
    nombres = ['Juan', 'Luisa', 'Ana', 'Pedro', 'Federico', 'Regina']
    fecNac = ['07/02/2004', '13/09/1991', '17/10/2012', '04/04/1963', '28/07/1998', '20/03/2010']
    return nombres, fecNac

n, f = carga()
mayores = []
edades_de_los_mayores = []
for x in range(len(n)):
    if edad(f[x]) >= 18:
        mayores.append(n[x])
        edades_de_los_mayores.append(edad(f[x]))
        print(n[x], 'tiene', edad(f[x])) 

print('los mayores de edad son: ',mayores)   
print('las edades de los mayores: ', edades_de_los_mayores)    