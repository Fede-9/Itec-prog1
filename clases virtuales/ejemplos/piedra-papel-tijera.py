import random
print(" ---- PIEDRA, PAPEL O TIJERA ----")
condicion = "empate"

while(condicion == "empate"):
    usuario = int(input("1- Piedra \n2- Papel \n3- Tijera \nIngrese el numero correspondiente al valor: "))
    computadora = random.randint(1,3)
    if(usuario == computadora):
        print("Valor computadora:", computadora)
        print("Valor usuario:", usuario)
        print("EMPATES, ingrese de vuelta su valor")
    elif((usuario == 1 and computadora == 3) or (usuario == 2 and computadora == 1) or (usuario == 3 and computadora == 2)):
        print("Valor computadora:", computadora)
        print("Valor usuario:", usuario)
        print("-- GANASTE --")
        condicion = "ganador"
    elif(usuario > 3):
        print("Numero mayor que 3, ingrese de nuevo el valor")
    else:
        print("Valor computadora:", computadora)
        print("Valor usuario:", usuario) 
        print("Perdiste")
