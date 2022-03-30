import locale
from datetime import datetime, timedelta, date

ahora = datetime.now() 

quinceDias = ahora + timedelta(days=15)
print(ahora.isoformat())
print(quinceDias.isoformat())

loc = locale.getlocale()
locale.setlocale(locale.LC_ALL, loc)

print(ahora.strftime("%a %d %B %Y %I:%M"))
print(ahora.strftime("%A %d de %B del %Y - %H:%M horas"))
print(ahora.strftime('Número de día en el año: %j'))
print(ahora.strftime('Número de semana en el año: %U'))
print(quinceDias.strftime("%A %d de %B del %Y - %H:%M horas"))
print(ahora.strftime("%A"))

print(ahora.month)

hoy = date.today()
for d in range(7):
    dia = hoy - timedelta(days=d)
    print(dia, dia.strftime("%A"))
