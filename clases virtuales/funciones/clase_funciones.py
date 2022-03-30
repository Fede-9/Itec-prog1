# Ejemplo de función de validación
# Pedir edad y altura de una persona.
# Mostrar el nombre si es menor de edad que mida más de 1.80 metros

def inputNumber(tipo, mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            if tipo == "entero":
                numero = int(numero)
            elif tipo == "real":
                numero = float(numero)
            else:
                print("Check! entero o real. Ctrl C!")
            validado = True
        except:
            print("Error. Debe ingresar un número", tipo)
    return numero

nombre = input("Nombre: ")
edad = inputNumber("entero", "Ingrese edad: ")
altura = inputNumber("real", "Ingrese altura: ")

if edad < 18 and altura > 1.80:
    print(nombre, "es menor de edad y mide", altura, "metros")