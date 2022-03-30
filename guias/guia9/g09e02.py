#(g02e04) Pedir el ingreso de 10 números y contar los mayores a 23.

import PySimpleGUI as sg



layout =[ #se crea el diseño
            [sg.Text('Ingrese 10 numeros: ')],
            [sg.Text('Numero: ', key='-NUM-'), sg.Input(key='-IN-')],
            [sg.Text('Numero ingresado'),sg.Text(key='-OUT-')],
            [sg.Text('Cantida de numeros ingresados: ', key='-CANT-')],
            [sg.Button('Cargar',bind_return_key=True),sg.Button('Reset'),sg.Button('Exit')],
]

window = sg.Window('winTitle', layout) # return_keyboard_events=True

nums = []

while True:
    event, values = window.read()
    print(values['-IN-'])
    if event in [None, 'Exit']:
        break
    elif event == 'Cargar':
        try:
            num = int(values['-IN-'])
            window['-OUT-'].update(num)
            nums.append(num)
            window['-CANT-'].update(f'Cantidad numeros ingresados: {len(nums)}')
        except:
            window['-OUT-'].update('No ingreso un numero')
    elif event == 'Reset':
        nums = []
        window['-OUT-'].update('')
        window['-CANT-'].update(f'Cantidad numeros ingresados: {len(nums)}')
    if len(nums) == 10:
        sg.popup(f'Numeros mayores a 23 ingresados: {[n for n in nums if n > 23]}')


    

window.close()
        
    