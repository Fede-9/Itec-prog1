#(g05e13) Pedir el ingreso de un nombre completo (Juan Pérez) y mostrarlo invertido y con coma (Pérez, Juan).
import PySimpleGUI as sg

layout = [
            [sg.Text('Ingrese nombre. Ejemplo: Juan Perez')],
            [sg.Input(key='nombre')],
            [sg.Button('OK'), sg.Button('Exit')]
            ]

def createGUI(lay):
    window = sg.Window('Inverso nombre', layout) # return_keyboard_events=True

    while True:
        event, values = window.read()
        if event in [None, 'Exit']:
            break
        elif event == 'OK':
            nameSplit = values['nombre'].split(' ')
            if len(nameSplit) == 2:
                sg.popup(f'{nameSplit[1].title()}, {nameSplit[0].title()}')
            else:
                sg.popup('No se ingreso el nombre con el formato pedido')
        

    window.close()

def main():
    createGUI(layout)

if __name__ == '__main__':
    main()