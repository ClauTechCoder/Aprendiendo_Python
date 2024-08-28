
# Ver concepto de fechas y como usar los diferentes formatos y tipos de las mismas.
# No es de tipo puro, es un objeto completo (codigo python + objs simples)

from datetime import datetime # importo datetime de su modulo/libreria para poder usarlo.
from datetime import time # importo time de su modulo/libreria para poder usarlo.
from datetime import date # importo date de su modulo/libreria para poder usarlo.
from datetime import timedelta # importo timedelta de su modulo/libreria para poder usarlo.

now = datetime.now() # creo una instancia de la fecha y hora actual

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp() # representa el momento actual en segundos desde 1/1/1970
print(timestamp)

# Crear una fecha concreta manualmente
year_2025 = datetime(2025, 12, 31,3,45,29)
print(year_2025)

# creo una funcion que me da todos los tiempos a una fehca que le pasemos
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(year_2025)

# no es lo mismo a datetime; solo tiene hora, minuto, segundo, y microsegundo. Solo la parte de las horas
current_time = time(21, 6, 0) # no asociado, hay que rellenarlo. Tbn se puede definir vacio
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.microsecond)

# no es lo mismo a datetime; solo tiene año, mes y día. Solo la parte de fecha.
current_date = date(2024, 7,21) # no asociado, hay que rellenarlo. Tbn se puede definir vacio
print(current_date.year)
print(current_date.month)
print(current_date.day)

# modificar fecha aprox, manera muy cutre mejor usar timedelta
current_date = date(current_date.year - 1, current_date.month, current_date.day + 1)
print(current_date.year)
print(current_date.month)
print(current_date.day)

# si son del mismo tipo puedo oeprar con esas fechas
diff = year_2025 - now
print(diff)

# usamos timedeltra para trabajar con franjas de fechas
start_timedelta = timedelta(200, 100, 100, weeks = 10) # si no sigo patron tengo que definir con el = a que me refiero
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta) # puedo operar facilmente. Permitido + - y /.

