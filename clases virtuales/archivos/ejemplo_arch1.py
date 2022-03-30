#CREAR ARCHIVO

#arch = open('data.txt', 'w') #sobreescritura sino existe lo crea.

#arch.close() # siempre cerrar el archivo


#ESCRIBIR EN EL ARCHIVO

# arch = open('data.txt', 'a')   #abriendo y creando
# arch.write('\ndesde Serrano')
# arch.write('\naguante bocaaa')
# arch.close()


#LEER UN ARCHIVO

# arch = open('data.txt', 'r')
# print(arch.read())
# arch.close()


#COMO LEER LINEA POR LINEA

# arch = open('data.txt', 'r')
# linea = arch.readline()  #creo una variable, el readline me sirve para leer la primera linea
# while linea != '':
#     print(linea)
#     linea = arch.readline()                     
# arch.close()


#OTRA MANERA DE LEER

arch = open('data.txt', 'r')
for x in arch.readlines():
    print(x)
arch.close()
