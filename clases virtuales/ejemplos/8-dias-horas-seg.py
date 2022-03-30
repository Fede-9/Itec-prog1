segundos = int(input("Ingrese la cantidad de segundos: "))
if(type(segundos) == int):  
    dias = segundos // 86400
    segundos = segundos % 86400
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
else:
    print("Valor inválido")


print("La cantidad de segundos ingresados representan: ")
print("--",dias, "dias", horas, "horas", minutos, "minutos", segundos, "segundos --")

                    