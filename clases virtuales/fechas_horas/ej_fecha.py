from datetime import datetime
import locale

ahora = datetime.now() 

loc = locale.getlocale()
locale.setlocale(locale.LC_ALL, loc)

print(ahora)
print('el mes actual es:', ahora.month)

print('hoy es:', ahora.strftime("%A"))