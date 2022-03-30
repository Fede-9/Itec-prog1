# importar la librería para interfaz gráfica
import PySimpleGUI as sg

# definir la estructura de presentación de la ventana
layout = [
            [sg.Text('Ingrese su nombre: '), sg.Input(key='nombre')],
            [sg.Text(size=(40,1), key='salida')],
            [sg.Button('Saludar'), sg.Button('Reirse'), sg.Button('Exit')]
            ]

# instanciar la ventana
window = sg.Window('Título de la ventana', layout)

# bucle principal de la aplicación
while True:
    # obtener el evento (string con el texto del botón)
    # obtener los valores(diccionario con los valores de los inputs)
    event, values = window.read()
    print("Event: ", event, type(event))
    print("Values:", values, type(values))
    
    # control de botón de fin de ejecución o bien cierre de la ventana
    if event in [None, 'Exit']:
        break
   
    if event == 'Saludar':
            #window['salida'].update(f"Hola {values['nombre']}") lo mismo que las 3 lineas siguientes
            nombre = values['nombre']
            saludo = "Hola " + nombre
            window['salida'].update(saludo)
    elif event == 'Reirse':
            window['salida'].update("jaaaaaaaaaaaaaaaaaaaaaa!!!!!")

# cerrar la ventana
window.close()