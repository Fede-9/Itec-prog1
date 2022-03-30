#Forma clásica de crear un archivo:
f = open("archivotext.txt", "w")  #Creamos el archivo
f.write("Creando archivo de texto en python de forma clásica") #Escribimos en el archivo creado
f.close()    #Cerramos el archivo

#Utilizando With As   otra forma de hacerlo
with open ("archivotext.txt", "w") as f: #Creamos el archivo
    f.write("Creando archivo de texto en python usando whit as") #Escribimos en el archivo creado
    f.close()
#Podria traducirse como:
#Abrir "archivotext.txt en modo Write como f.