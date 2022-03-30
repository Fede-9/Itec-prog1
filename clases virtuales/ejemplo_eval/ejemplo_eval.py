print(eval('2+1'))

def f():
    return "salida de f"

print(eval('f()'))

def g(v):
    print('función g con valor', v)

otraFun = "g"
eval(otraFun + "(3)")
eval('g(17)')

eval('print("hola")')
