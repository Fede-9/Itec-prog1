# Base para dos ventanas, ambas abiertas y con eventos.

import PySimpleGUI as sg


def firstLayout():
    filas = [
        [
            sg.Text("Cuántas personas se van a cargar: ", size=(30, 1)),
            sg.Input(key="entero_cantidad", size=(3, 1)),
        ],
        [sg.Button("Ok", bind_return_key=True), sg.T("", key="msg", size=(30, 1))],
    ]
    return filas


def secondLayout(values):
    filas = [
        [
            sg.Text(f"Edad de la persona {fila+1}: ", size=(30, 1)),
            sg.Input(key=f"entero_edad_{fila+1}: ", size=(3, 1)),
        ]
        for fila in range(int(values["entero_cantidad"]))
    ]
    filas.append(
        [sg.Button("Ok", bind_return_key=True), sg.T("", key="salida", size=(30, 1))]
    )
    return filas


def validate_input(window, values, msg):  # Define la validacion de los datos ingresados
    vD = {"entero": int, "real": float}
    for k, v in values.items():
        tipo = k.split("_")[0]
        if tipo in vD:
            try:
                vD[tipo](v)
                window[msg].update(value="")
            except:
                window[msg].update(value=f"Error: Debe ser un {tipo}")
                window[k].set_focus()
                return False
    return True


def main(firstWindow):
    def wLoop(window, fAction, msg):
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break
            if validate_input(window, values, msg):
                fAction(window, values)

    def action2(secondWindow, values2):
        lista = [int(x) for x in values2.values()]
        promedio = f"El promedio es {sum(lista) / len(lista)}"
        secondWindow["salida"].update(str(promedio))

    def action1(firstWindow, values1):
        firstWindow["msg"].update("Abrí la segunda ventana")
        secondWindow = sg.Window(
            "Edades", layout=secondLayout(values1), location=(200, 200)
        )
        wLoop(secondWindow, action2, "salida")

    wLoop(firstWindow, action1, "msg")


if __name__ == "__main__":
    firstWindow = sg.Window("Promediar edades", firstLayout(), location=(0, 0))
    main(firstWindow)
    firstWindow.close()