#(g04e10) Determinar cuál es la vocal que aparece con mayor frecuencia en una frase.

#RESOLUCION DE EJERCIO EN LA OTRA GUIA

# lista = [frase.count(v) for v in vocales]
# print(lista)
# for i in range(len(lista)):
#     if lista[i] == max(lista):
#         print(vocales[i])


import PySimpleGUI as sg


def layout():  # Define la interfaz grafica
    lista = [
        [sg.Text("Ingrese una frase: ", size=(30, 1)), sg.Input(key="frase")],
        [sg.Button("Vocales", bind_return_key=True)],
        [sg.Text("", size=(30, 1), key="salida")]
    ]
    return lista


def main(window):
    while True:
        event, values = window.read()
        if event in (None, "Quit"):
            break

        frase = values["frase"]
        vocales = "aeiou"
        lista = [frase.count(v) for v in vocales]
        print(lista)
        salida = "Las vocales más frecuentes son: " 
        for i in range(len(lista)):
            if lista[i] == max(lista):
                salida += " " + vocales[i]
        window["salida"].update(salida)

if __name__ == "__main__":
    w = sg.Window("Title", layout())
    main(w)
    w.close()

