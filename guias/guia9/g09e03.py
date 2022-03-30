# Preguntar cuántas personas se van a cargar y luego solicitar sus edades,
# mostrando al final la edad promedio.

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
        [sg.Button("Ok", bind_return_key=True), sg.T("", key="msg", size=(30, 1))]
    )
    return filas


def validate_input(window, values):  # Define la validacion de los datos ingresados
    vD = {"entero": int, "real": float}
    for k, v in values.items():
        tipo = k.split("_")[0]
        if tipo in vD:
            try:
                vD[tipo](v)
                window["msg"].update(value="")
            except:
                window["msg"].update(value=f"Error: Debe ser un {tipo}")
                window[k].set_focus()
                return False
    return True


def main(window):
    def wLoop(window, fAction):
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Quit"):
                break
            if validate_input(window, values):
                fAction(window, values)

    def action2(window, values):
        lista = [int(x) for x in values.values()]
        promedio = f"El promedio es {(sum(lista) / len(lista)):.2f}"
        window["msg"].update(promedio)

    def action1(window, values):
        window.close()
        window = sg.Window("Edades", secondLayout(values))
        wLoop(window, action2)

    wLoop(window, action1)


if __name__ == "__main__":
    w = sg.Window("Promediar edades", firstLayout())
    main(w)
    w.close()