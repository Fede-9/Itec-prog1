def f1():
    print('++++++++++++++++')
f1()
print('Hola')
f1()

def f2():
    return '===================='
print(f2())

def f3(n):
    return n * 2
print(f3(2))
print(f3('hola'))

def f4(nombre, edad):
    print('Hola', nombre, 'tenés', edad, 'años')
f4('Juan', 31)

def f5(nombre, edad=1000):
    print(nombre, edad)
f5('Juan', 31)
f5('Pablo')