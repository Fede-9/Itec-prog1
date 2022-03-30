#Preguntar cuántas personas se van a cargar y luego solicitar sus edades, mostrando al final la edad promedio.
edad1 = 0
num_cargas = int(input("Cuantas peresonas van a cargar?: "))
for x in range(num_cargas):
    edad2 = int(input("ingrese du edad: "))
    edad1 += edad2
promedio = edad1 / num_cargas
print("El promedio de edad es de:", promedio)
