#Ingresar la lluvia caída en milímetros para cada día de la semana.
 #Mostrar al final el total de lluvia caída y el nombre del día que más llovió. 
 #(Todos los días llovió distinta cantidad)

dia = []
lluvia = []
total = 0

for x in range(1,8):
    x = input("ingrese dia de la semana: ")
    dia.append(x)
    x = int(input("ingrese la cantida de lluvia en milimetros: " ))
    lluvia.append(x)
    total+=x


    
mas_llovio = ''
cont = 0

for x in range(len(lluvia)):
    if (lluvia[x] > cont):
        cont = lluvia[x]
        mas_llovio = dia[x]


print("Total de lluvia caída: ",total)
print("Dia que mas llovio: ", mas_llovio)

