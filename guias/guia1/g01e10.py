"""	10-Preguntar nombre, carrera en la que se inscribe y ciudad donde vive un ingresante al Instituto.
 Los estudiantes de la carrera de Electromecánica y que no viven en Río Cuarto tendrán un 15% de descuento 
 en la cuota que es de $4500. 
 Mostrar nombre, ciudad, carrera y monto final de la cuota. """

nombre = input("Ingrese nombre: ")
carrera = input("en que carrera te inscribes?: ")
ciudad = input("en que ciudad vives?: ")
cuota = int(4500)
if (carrera == "electromecanica") and (ciudad != "rio cuarto"):
    print('nombre:',nombre,'ciudad:',ciudad,'carrera:',carrera, "monto de la cuota:", cuota*0.85)
else:
    print(nombre, ciudad, carrera, "monto de la cuota", cuota)
