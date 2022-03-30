""" 12-	Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y  cuya 
antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000).
 Pedir la cantidad de días no trabajados y año de ingreso en la empresa."""
 
dias_que_no_trabajo = int(input("cuantos dias usted no trabajo?: "))
año_de_ingreso = int(input("en que año usted ingreso en la empresa?: "))
año_actual = int(2021)
antiguedad = año_actual-año_de_ingreso
sueldo_basico = int(47000)
if (antiguedad > 5) and (dias_que_no_trabajo == 0):
    print("su sueldo a cobrar es de", sueldo_basico*1.3)
else:
    print("su sueldo a cobrar es de", sueldo_basico) 
