import PySimpleGUI as sg 
sg.theme("Kayak")

listado = [["Damian",1536],["Pepe",1590], ["Alberto",2549], ["Cristina",1225]]
mi_lista = sorted(listado)

def ventana_uno():
    columnas = [
        [sg.Stretch(), sg.Text('Nombre y sueldos de los empleados'), sg.Stretch()],
        [sg.Stretch(), sg.Listbox(mi_lista, size = (40, 7), key = '-LISTADO-'), sg.Stretch()],
        [sg.Stretch(), sg.Button('Agregar'),sg.Button('Modificar'), sg.Button('Borrar'), sg.Stretch()]
        ]
    return sg.Window("",columnas, finalize=True)

def ventana_dos():
    columnas = [
        [sg.Stretch(), sg.Text('Cual es el nombre?', key = '-AGREGADO-'), sg.Stretch()],
        [sg.Input(key = '-INPUT1-', size = (40,1))], 
        [sg.Stretch(),sg.Text('Cual es el sueldo?'), sg.Stretch()],
        [sg.Input(key = '-INPUT2-', size =(40,7))],
        [sg.Stretch(), sg.Button('Aceptar'), sg.Button('Cancelar'), sg.Stretch()]
        ]
    return sg.Window("",columnas, finalize=True)



def main():
    uno, dos = ventana_uno(), None
    añadir = False
    modificar = False
    while True:
        window, event, values = sg.read_all_windows()
        if window == uno and event == sg.WIN_CLOSED:
            break
      
      
        if window == uno and event == 'Agregar':
            añadir = True
            dos = ventana_dos()
            dos.un_hide()
        if window == dos and event == 'Aceptar' and añadir == True:
            mi_lista.append([values['-INPUT1-'],values['-INPUT2-']])
            uno['-LISTADO-'].update(mi_lista)
            añadir = False
            dos.hide()


        if window == uno and event == 'Modificar':
            modificar = True
            posicion = mi_lista.index(values['-LISTADO-'][0])
            dos = ventana_dos()
            dos.un_hide()    
            dos['-AGREGADO-'].update('Modificar')
            dos['-INPUT1-'].update(values['-LISTADO-'][0][0]) 
            dos['-INPUT2-'].update(values['-LISTADO-'][0][1])
        if window == dos and event == 'Aceptar' and modificar == True:
            mi_lista[posicion] = [values['-INPUT1-'],values['-INPUT2-']] 
            uno['-LISTADO-'].update(mi_lista)
            modificar = False
            dos.hide()
      
      
        if window == uno and event == 'Borrar':
            posicion = mi_lista.index(values['-LISTADO-'][0])
            mi_lista.pop(posicion)
            window['-LISTADO-'].update(mi_lista)
        if window == dos and (event == 'Cancelar' or event == sg.WIN_CLOSED):
            dos.hide()
            uno.un_hide()  
    

if __name__ == '__main__':
    main()