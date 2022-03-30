from zoneinfo import ZoneInfo
from datetime import datetime
 
tz = ZoneInfo("America/Buenos_Aires") 
fecha = datetime(2021, 1, 28, 23, tzinfo=tz)
print(fecha) 
print(fecha.tzname()) 