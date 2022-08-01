#Sin el decorador, habríamos de hacerlo de la forma tradicional:
print('------------------ SIN Y CON EL MODULO DATACLASS -----')

class Deportista():
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

deportista1 = Deportista('Elena', 1.81, 64)
print(deportista1.altura)  # 1.81



# Con el modulo dataclasses permite escribir la clase anterior:
#Como puede observarse a la clase Deportista le precede el decorador dataclass y no tiene definido el método __init__().
# Una de las funciones del decorador es localizar las variables de clase que llevan anotaciones de tipos para 
# conocer los campos que tiene la clase de datos. 
# Después, con respecto al modo de instanciar la clase no se advierte ningún cambio con respecto al uso habitual.

from dataclasses import dataclass

@dataclass #decorador
class Deportista():
    nombre: str 
    altura: float
    peso: float

deportista1 = Deportista('Elena',1.81, 64)
print(deportista1.altura)  # 1.81


print('---------------  METODOS DE DATACLASS ----------------')

# Sabemos que el decorador genera el método __str__() (que devuelve una cadena con una representación legible de los datos)
#  porque es llamado cuando se imprime el objeto o cuando se hace uso de la función str():

print(deportista1)  # Deportista(nombre='Elena', altura=1.81, peso=64)

atleta = str(deportista1)  
print(atleta)  # Deportista(nombre='Elena', altura=1.81, peso=64)


@dataclass
class Deportista:
    nombre: str
    altura: float
    peso: float
    
    def __str__(self):
        return f'{self.nombre}: {self.altura}, {self.peso}'

deportista1 = Deportista('Elena', 1.81, 64)
print(deportista1)  # Elena: 1.81, 64



print('-------------- PARAMETROS DE DATACLASS ----------')


#El decorador dataclass cuenta también con varios parámetros para ajustar su funcionamiento:

# @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
           

# - init, repr y eq: Por defecto estos parámetros tienen el valor True para que el decorador genere 
# los métodos __init__(), __repr__() y __eq__(), respectivamente, aunque si la clase los redefine serán ignorados.
# - order: Por defecto tiene el valor False pero si se establece a True el decorador generará los métodos 
# especiales __gt__(), __ge__(), __lt__() y __le__(). 
# En este caso no se permite la reescritura, por lo que si la clase redefine alguno de ellos se producirá una excepción.
# - unsafe_hash: Por defecto tiene el valor False y en este caso el decorador generará el método __hash__() de acuerdo a la 
# configuración que tengan los parámetros eq y frozen.
# - frozen: Por defecto tiene el valor False pero si se establece a True cualquier intento de asignación a los campos producirá una excepción.


# EJEMPLO:

# En el siguiente ejemplo se establece el parámetro order con el valor True para que el 
# decorador dataclass genere los métodos __gt__(), __ge__(), __lt__() y __le__() que se corresponden con 
# las comparaciones "mayor que", "mayor o igual que", "menor que" y "menor o igual que", respectivamente.

@dataclass(order=True)
class Deportista:
    nombre: str = 'Desconocido'
    altura: float = 0
    peso: float = 0

deportista1 = Deportista(peso=64)
deportista2 = Deportista(peso=62)
deportista3 = Deportista(peso=67)

print(deportista1 > deportista2)  # True
print(deportista1 > deportista3)  # False


# OTRO EJEMPLO:

# En el ejemplo siguiente se establece el parámetro frozen a True con lo cual es posible instanciar la clase 
# para crear objetos pero no es posible asignar valores porque el objeto ha sido "congelado". 
# El intento de asignación produce una excepción de tipo dataclasses.FrozenInstanceError:

@dataclass(frozen=True) 
class Deportista:
    nombre: str = 'Desconocido'
    altura: float = 0
    peso: float = 0

deportista1 = Deportista(peso=64)
#deportista1.peso = 63   da error



print('------------------- FUNCION asdict() -----------------')

# La función asdict() se utiliza para convertir una instancia de clase de datos en un diccionario Python.

# En el ejemplo siguiente se importa la función asdict que se emplea para convertir el objeto deportista1 en 
# un diccionario usando los campos de la clase de datos para definir sus claves y sus valores:


from dataclasses import dataclass, asdict

@dataclass
class Deportista:
    nombre: str
    altura: float
    peso: float

deportista1 = Deportista('Elena', 1.81, 64)
dicc1 = asdict(deportista1)

if dicc1['altura'] > 1.75:
   print(dicc1['nombre'], 'supera la altura')



print('----------------- FUNCION field() ----------------')

# La función field() permite facilitar información adicional al decorador relativa a cada campo que la utilizará en la generación de los métodos.

# En el ejemplo que sigue para el atributo peso se establecen los parámetros init y repr a False. 
# Esto indica al decorador que el objeto podrá crearse sin el atributo peso y que cuando se imprima su 
# representación será omitida esta información. 
# No obstante, como el atributo peso existe se le podrá asignar un valor en cualquier momento y acceder al mismo después de la asignación.


from dataclasses import dataclass, field

@dataclass
class Deportista:
    nombre: str
    altura: float
    peso: float = field(init=False, repr=False)

deportista1 = Deportista('Elena', 1.81)
deportista1.peso = 64
print(deportista1)  # Deportista(nombre='Elena', altura=1.81)
print(deportista1.peso)  # 64



