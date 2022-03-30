# (g01e01) Pedir dos números enteros, sumarlos y mostrar el resultado.
import PySimpleGUI as sg #importar libreria

layout = [
            [sg.Text('Ingrese un número:'), sg.Input(key='n1')],
            [sg.Text('Ingrese otro número'), sg.Input(key='n2')],
            [sg.Text(key='salida', size=(30, 1))],
            [sg.Button('Suma'), sg.Button('Exit')]
            ]

window = sg.Window('Suma', layout)

while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    s = f'La suma es {int(values["n1"]) + int(values["n2"])}'
    window['salida'].update(s)

window.close()