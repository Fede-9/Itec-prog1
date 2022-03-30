def app():
    # Crear el archivo
    archivo = open('archivo.txt', 'w') # w es escritura, si no existe el archivo.txt lo creara

    # Generar numeros en archivo
    for i in range(0, 20):
        archivo.write('Esta es la linea' + str(i) +  '\r\n')

    # Cerrar el archivo
    archivo.close()

app()