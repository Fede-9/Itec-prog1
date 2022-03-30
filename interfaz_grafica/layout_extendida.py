import PySimpleGUI as sg


def layout():  # Define la interfaz grafica
    # Ejemplo de Pantalla
    lista = [
        [sg.Text("Nombre: ", size=(10, 1)), sg.Input(key="nombre")],
        [sg.Text("Vehículo: ", size=(10, 1)), sg.Input(key="vehículo")],
        [sg.Button("Click aquí para agregar más vehículos")]
    ]
    
    return lista


def main(window):
    c = 0
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Quit"):
            break
        print(event, values)
        if event == "Click aquí para agregar más vehículos":
            c += 1
            window.extend_layout(
                window,
                [
                    [
                        sg.T(f"Vehículo adicional {c}: ", size=(20, 1)),
                        sg.I(key=f"vehículo{c}"),
                    ]
                ],
            )


if __name__ == "__main__":
    w = sg.Window("Ventana expandible", layout())
    main(w)
    w.close()