import PySimpleGUI as sg


def layout():  # Define la interfaz grafica
    # Ejemplo de Pantalla
    lista = [
        [sg.Text("Nombre: ", size=(10, 1)), sg.Input(key="nombre")],
        [sg.Text("Edad: ", size=(10, 1)), sg.Input(key="entero_edad")],
        [sg.Text("Puesto: ", size=(10, 1)), sg.Input(key="puesto")],
        [sg.Text("Altura: ", size=(10, 1)), sg.Input(key="real_altura")],
        [sg.Button("Ok", bind_return_key=True), sg.T("", key="msg", size=(30, 1))],
    ]
    lista.append([sg.Text("", key="salida", size=(30, 1))])
    return lista


def main(window):
    def validate_input(values):  # Define la validacion de los datos ingresados
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

    def valid_main():
        """Algoritmo Principal Validado"""
        # Ejemplo
        s = f'El doble de la edad es {int(values["entero_edad"])*2}'
        window["salida"].update(s)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Quit"):
            break
        if validate_input(values):
            valid_main()


if __name__ == "__main__":
    w = sg.Window("Title", layout())
    main(w)
    w.close()