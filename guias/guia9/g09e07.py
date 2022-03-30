#(g03e11) Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo 
#y mostrar los nombres de los mayores de edad.

import PySimpleGUI as sg
from dataclasses import dataclass
from datetime import datetime

def edad(fn, separador):
    """ Convierte la fecha de una persona en edad"""
    hoy = datetime.today()
    try:
        dn, mn, an = fn.split(separador)
        dn = int(dn)
        mn = int(mn)
        an = int(an)
        dh = hoy.day
        mh = hoy.month
        ah = hoy.year
        e = ah - an
    except:
        return 'Separador incorrecto'
    else:
        if (mn > mh) or (mn == mh and dn > dh):
            e -= 1
        return e


@dataclass
class Persona:
    nombre:str
    nacimiento:int
    
    
    def getNombre(self):
        return self.nombre.title()
    
    
    def getNacimiento(self):
        return self.nacimiento
    
    def getEdad(self):
        """ Edad de una persona"""
        hoy = datetime.today()
        try:
            dn, mn, an = self.nacimiento.split('/')
            dn = int(dn)
            mn = int(mn)
            an = int(an)
            dh = hoy.day
            mh = hoy.month
            ah = hoy.year
            e = ah - an
        except:
            return 'Separador incorrecto'
        else:
            if (mn > mh) or (mn == mh and dn > dh):
                e -= 1
            return e
        

layout = [
            [sg.Stretch(),sg.Text('Cantidad de personas a cargar: '),sg.Stretch()],
            [sg.Stretch(),sg.Input(key='-CANT-'),sg.Stretch()],
            [sg.Stretch(),sg.Button('Cargar'), sg.Button('Exit'),sg.Stretch()],
            ]

def createGUI(lay):
    window = sg.Window('Mayores de edad', lay) # return_keyboard_events=True

    while True:
        event, values = window.read()
        if event in [None, 'Exit']:
            break
        elif event == 'Cargar':
            try:
                # Control de int
                cantPersonas = int(values['-CANT-'])
                i = 1
                people = []
                while int(cantPersonas) > 0:
                    # Display para los input
                    nombre = (sg.popup_get_text(f'Nombre de la persona {i}: '))
                    nacimiento = (sg.popup_get_text(f'Nacimiento de la persona {i} (dd/mm/aaaa): '))
                    age = edad(nacimiento, '/')
                    
                    while type(age) != int:
                        nacimiento = (sg.popup_get_text(f'Nacimiento de la persona, incorrecto, intente nuevamente. (dd/mm/aaaa): '))
                        age = edad(nacimiento, '/')
                    people.append(Persona(nombre, nacimiento))
                    i += 1 
                    cantPersonas -= 1
            except:
                # Except si no ingresa int
                sg.popup(f'Ingreso un valor invalido')
            else:
                # Filtro mayores de edad
                mayoresEdad = [p for p in people if p.getEdad() >= 18]
                displayText = 'Mayores de edad:\n' # Texto para el popup
                for p in mayoresEdad:
                    displayText += f'{p.getNombre()}, {p.getEdad()} anios\n'
                sg.popup(displayText) # Texto ya armado para el popup
            
    window.close()
    
def main():    
    createGUI(layout)

    

if __name__ == '__main__':
    main()