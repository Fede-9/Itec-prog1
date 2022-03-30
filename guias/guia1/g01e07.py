#7- Pedir un nombre y una opción ('>' o '<') y según esta mostrar por ejemplo.: Juan es menor de edad.

nombre = input("digame su nombre: ")
edad = input("sos'>' o '<' de edad?: " )
if (edad == ">"):
    print(nombre, "es mayor de edad")
elif (edad == "<"):
    print(nombre, "es menor de edad")