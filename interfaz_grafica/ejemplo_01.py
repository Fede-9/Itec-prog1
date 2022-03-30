import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Crea la ventana
window = sg.Window("Demo", layout)

# Crea un bucle de eventos
while True:
    event, values = window.read()
    # si presiona ok o cierra el programa finaliza
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()