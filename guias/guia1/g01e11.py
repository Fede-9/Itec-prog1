""" 11-	El costo del pasaje a Córdoba es de $1700.
La empresa realiza un descuento de un 40 % sobre el costo del boleto a los niños que tienen entre
 5 y 10 años y a los jubilados (mayores de 65).
 Pedir nombre y edad y mostrar el nombre y el valor final del pasaje."""
 
nombre = input("cual es tu nombre?: ")
edad = int(input("que edad tenes?: "))
pasaje = int(1700)
if (edad >= 5) and (edad <= 10) or (edad > 65):
    print(nombre, pasaje*0.80)
else:
    print(nombre, pasaje) 

