import PySimpleGUI as sg
from random import randint


sg.theme('DarkAmber')


layoutUno =[
        [sg.Stretch(), sg.Text('¡ TE ESTABAMOS ESPERANDO !'), sg.Stretch()],
        #[sg.Stretch(),sg.Image[],sg.Stretch()],
        [sg.Stretch(),sg.Button('INICIAR',size=(15,2),button_color=('#CC6600')),
        sg.Button('INSTRUCCIONES',size=(15,2),button_color=('#CC6600')),sg.Stretch()]
        
]
        
windowUno = sg.Window('BIENVENIDO A LA PLATAFORMA', layoutUno, size=(400,100))



layoutDos = [
        [sg.Stretch(), sg.Text('Elija una opción'), sg.Stretch()],
        [sg.Stretch(), sg.Radio(f' {"PAR"}', "eleccion", default=True),sg.Radio(f' {"IMPAR"}', "eleccion",default=True ), sg.Stretch()],
        [sg.Text('Escriba su número'), sg.Input(size=(9, 1))],
        [sg.Stretch(), sg.Button('JUGAR',button_color=('#CC3300')), sg.Button('RESUMEN',button_color=('#009900')), sg.Stretch()],
]

window = sg.Window('ADIVINA ADIVINADOR', layoutDos, size=(400,150))




juegoGanado = 0 
juegoPerdido = 0 


while True:
    event, values = windowUno.read()
    if event == sg.WIN_CLOSED:
        break 

    if event == 'INSTRUCCIONES':
        sg.popup('El juego consiste en adivinar si el resultado de la suma del número ingresado\
 por usted y la computadora es PAR o IMPAR, siempre hay un ganador.',title='¿Cómo ganar?')
        
    

    if event == 'INICIAR':

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
                
                
                
            if event == 'RESUMEN':
                sg.popup(f'Partidas ganadas por el usuario: {juegoGanado}\nPartidas ganadas por la computadora: {juegoPerdido}',title='Historial')

            if event == 'JUGAR':

                while True:
                    computadora = randint(0, 100)        
        
                    if values[0] == True:
                        eleccionUsuario = 'PAR'
                        eleccionComputadora = 'IMPAR'
                    else:
                        eleccionUsuario = 'IMPAR'
                        eleccionComputadora = 'PAR'
                    suma = int(values[2]) + computadora
        
                    if suma % 2 == 0:
                        resultado = 'PAR'
                    else:
                        resultado = 'IMPAR'  
        
        
                    if eleccionUsuario == resultado:
                        window.hide()
                        sg.popup(f'El número que seleccionaste es el: {values[2]}\
                            La computadora selecciono el número: {computadora}\
                                La suma de los números es: {suma} ({resultado})\
                                    Tú eleccion: {eleccionUsuario}\
                                        Eleccion de la computadora: {eleccionComputadora}\
                                            {"¡¡USTED GANÓ EL JUEGO!!"}', title = '¡GANASTE!')
                        window.UnHide()
                        juegoGanado += 1
                
                    else:
                        window.hide()
                        sg.popup(f'El numero que seleccionaste es el: {values[2]}\
                            La computadora selecciono el número: {computadora}\
                                La suma de los números es: {suma} ({resultado})\
                                    Tú eleccion: {eleccionUsuario}\nEleccion de la computadora:  {eleccionComputadora}\
                                        {"¡¡USTED PERDIÓ EL JUEGO!!"}', title = "¡PERDISTE!")
                        window.UnHide()
                        juegoPerdido += 1
                        break

            
            
window.close()
windowUno.close()
sg.popup('¡¡¡GRACIAS POR JUGAR!!!')     