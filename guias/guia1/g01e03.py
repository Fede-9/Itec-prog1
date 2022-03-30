#3- Leer un numero real y emitir una leyenda informando si es mayor o igual a cero o bien es negativo 
# (son dos opciones).

numero_real = int(input("ingrese un numero: "))
if numero_real > 0:
 print("el numero real es mayor a 0")
elif numero_real == 0:
    print("el numero real es igual que 0")
else:
    print("el numero real es negativo")
    
