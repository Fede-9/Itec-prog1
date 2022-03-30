#(g03e10) Ingresar la lluvia caída en milímetros para cada día de la semana. 
#Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

import PySimpleGUI as sg
#from val_int import validacionEntero as vInt
layout = [
            [sg.Stretch(),sg.Text('Clima en la semana'), sg.Stretch()],
            [sg.Stretch(),sg.Text('Ingrese debajo lluvia del dia lunes',key='dia'), sg.Stretch()],
            [sg.Input(key='lluvia')],
            [sg.Stretch(),sg.Button('Continuar'), sg.Button('Exit'), sg.Button('Reiniciar'), sg.Stretch()]
            ]

dias = ['Lunes', 'Martes', 'Miercoles','Jueves','Viernes', 'Sabado', 'Domingo']
def createGUI(lay):
    lluvias = []
    i = 1
    sg.theme('Green')
    """ Recibe layout, aca adentro se realiza la logica, layout de manera global"""
    window = sg.Window('Clima', lay) # return_keyboard_events=True
    while True:
        event, values = window.read()
        if event in [None, 'Exit']:
            break
        if event == 'Reiniciar':
            lluvias = []
            i = 1
            window['dia'].update('Ingrese debajo lluvia del dia lunes')
        elif event == 'Continuar':
                try:
                    cLluvia = int(values['lluvia'])
                except:
                    sg.popup('Valor incorrecto')
                else:
                    lluvias.append(cLluvia)
                    window['dia'].update(f'Ingrese lluvia del dia {dias[i].lower()}')
                    if i < 6:
                        i = i + 1
                    if len(lluvias) == 7: 
                        maxLluvia = max(lluvias)
                        posLluvia = lluvias.index(maxLluvia)
                        sg.popup(f'Total lluvia caida: {sum(lluvias)} mm\nDia que más llovio: {dias[posLluvia].lower()}')
                    

    window.close()

def main():
    """ Funcion main"""
    createGUI(layout)

if __name__ == '__main__':
    main()