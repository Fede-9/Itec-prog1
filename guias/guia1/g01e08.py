#8- Pasar un período expresado en segundos a un período expresado en días, horas, minutos y segundos.
segundos = int(input("ingrese una banda de segundos: "))
dias = segundos // 86400
resto = segundos * 86400
horas = resto // 3600
resto = resto * 3600
minutos = resto // 60
segundos = resto * 60

print(dias, 'dias', horas, 'horas', minutos, 'minutos', segundos, 'segundos' )

