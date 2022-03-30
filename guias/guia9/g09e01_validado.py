import PySimpleGUI as sg

def layout():
    lista = [
        [sg.Text('Número 1: ', size=(10, 1)), sg.Input(key='entero_n1')], 
        [sg.Text('Número 2: ', size=(10, 1)), sg.Input(key='entero_n2')], 
        [sg.Button('Sumar', bind_return_key=True), sg.Text('', key='salida', size=(30, 1))]
        ]
    return lista

def main(window):
    def validate_input(values): 
        vD = {'entero': int, 'real': float}
        for k, v in values.items():
            tipo = k.split('_')[0]
            if tipo in vD:
                try:
                    vD[tipo](v)
                except:
                    window[k].update(value=f'Error: Debe ser un {tipo}')
                    window[k].set_focus()
                    return False
        return True

    def valid_main():
        """Algoritmo Principal Validado"""
        s = f'La suma es {int(values["entero_n1"]) + int(values["entero_n2"])}'
        window['salida'].update(s)

    while True:
        event, values = window.read()
        if event ==sg.WIN_CLOSED: 
            break
        if validate_input(values):
            valid_main()

if __name__ == '__main__':
    w = sg.Window('Sumar dos números', layout())
    main(w)
    w.close()