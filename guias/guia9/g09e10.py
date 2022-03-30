#(g05e09) Dada una lista cargada con números enteros, obtener el promedio de ellos. 
#Mostrar por pantalla dicho promedio y los números ingresados que sean mayores que él.

import PySimpleGUI as sg

numeros = [10,2,30,4,56,23]

layout = [
            [sg.Stretch(),sg.Text('Numeros en la lista'),sg.Stretch()],
            [sg.Stretch(),sg.Text(numeros),sg.Stretch()],
            [sg.Stretch(),sg.Button('Promedio'),sg.Button('> al promedio'),sg.Button('Exit'),sg.Stretch()]
            ]

def createGUI(lay):
    window = sg.Window('Promedio desde lista', layout) # return_keyboard_events=True
    promedio = sum(numeros) / len(numeros)
    mPromedio = [n for n in numeros if n > promedio]
    while True:
        event, values = window.read()
        if event in [None, 'Exit']:
            break
        elif event in 'Promedio':
            sg.popup(f'Promedio de los numeros de la lista {promedio}')
        elif event in '> al promedio':
            sg.popup(f'Promedio: {promedio}\nNumeros mayores al promedio:\n{mPromedio}')
            
        
        

    window.close()

def main():
    createGUI(layout)

if __name__ == '__main__':
    main()