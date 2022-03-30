#(g02e10) Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo  y 
# mostrar el nombre de la persona que menos gana.

import PySimpleGUI as sg
from dataclasses import dataclass
import PySimpleGUI as sg

@dataclass(order=True)
class Empleado:
    nombre:str
    salario:int
    
    def getSalario(self):
        return self.salario
    
    def getNombre(self):
        return self.nombre
    

layout_column = [
            [sg.Text('Nombre de la empresa')],
            [sg.Text('Empleados a cargar', size=(15,1)), sg.Spin([i for i in range(0, 100)],key='cant_empleados', size=(5,1))],
            [sg.Text(key='alert')],
            [sg.Button('Cargar'), sg.Button('Salir')]
            ]


layout = [[sg.Column(layout_column, element_justification='c')]]

window = sg.Window('Carga empleados', layout) # return_keyboard_events=True

while True:
    event, values = window.read()
    print(event)
    if event in [None, 'Salir'] or event == sg.WIN_CLOSED:
        break
    elif event == 'Cargar':
        try:
            cantEmpleados = int(values['cant_empleados'])
            print(cantEmpleados)
            if cantEmpleados < 0:
                window['alert'].Update('La cantidad de usuarios no puede ser menor a 0')
        except:
            sg.popup('Valores incorrectos / interrupcion por parte del usuario')
        else:
            emp = []
            i = 1
            try:
                while cantEmpleados > 0:
                    nEmpleado = sg.popup_get_text(f'Nombre empleado {len(emp) + 1}: ')
                    sEmpleado = int(sg.popup_get_text(f'Sueldo empleado {len(emp) + 1}: '))
                    emp.append(Empleado(nEmpleado,sEmpleado))
                    cantEmpleados -= 1 
                    window['alert'].Update('')
                if len(emp) > 0:
                    sMin = min([e.getSalario() for e in emp])
                    for e in emp:
                        if e.getSalario() == sMin:
                            window['alert'].Update(f'La persona con salario minimo es {e.getNombre()}, con un sueldo de ${e.getSalario()}') 
            except:
                sg.popup('Datos incorrectos')
                
            
window.close()

