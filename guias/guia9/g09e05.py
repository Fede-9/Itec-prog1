#(g03e03) Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
#Recorrerlas y mostrar los nombres de las mujeres. 

import PySimpleGUI as sg
from dataclasses import dataclass

@dataclass
class Persona:
    nombre:str
    genero:str

    def getGenero(self):
        return self.genero

    def getNombre(self):
        return self.nombre.title()

layout = [
            [sg.Text('Cantidad de personas a cargar: ')],
            [sg.Input(key='-CANT-')],
            [sg.Button('Cargar'), sg.Button('Exit')],
            
            
            ]

def createGUI(lay):
    window = sg.Window('Filtrado mujeres', lay) # return_keyboard_events=True

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
                    genero = (sg.popup_get_text(f'Genero de la persona {i} (h/m): '))
                    while genero not in 'hm':
                        genero = (sg.popup_get_text(f'Genero incorrecto, intente nuevamente (h/m): '))
                    people.append(Persona(nombre, genero))
                    i += 1 
                    cantPersonas -= 1
            except:
                # Except si no ingresa int
                sg.popup(f'Ingreso un valor invalido')
            else:
                # Filtrado de mujeres
                mujeres = [p for p in people if p.getGenero() == 'm']
                displayText = 'Mujeres:\n' # armado de texto para el popup
                for m in mujeres:
                    displayText += f'{m.getNombre()}\n'
                sg.popup(displayText)
            
    window.close()
    
def main():
    createGUI(layout)

if __name__ == '__main__':
    main()