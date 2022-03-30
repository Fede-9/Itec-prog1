import PySimpleGUI as sg

filas = [
            [sg.T('Ingrese su nombre:'), sg.I()],
            
            [sg.Button('OK')]
    ]

w = sg.Window('Super sencillo', filas)

event, values = w.read()
print(event, values)
w.close()
