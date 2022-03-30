# Agregación y Composición. 
# Ambos conceptos tienen la misma implementación: la instanciación de una clase al interior de otra. 
# La diferencia tiene que ver con la necesidad de la existencia de los objetos. 
# Pero en términos prácticos funcionan de manera similar. 
# Por tanto, de ahora en más nos vamos a referir a esta operación solamente como composición.

class Empleado():
    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self): # obtener nombre / retorna el nombre
        return self.nombre


class Empresa():
    def __init__(self):
        self.lista = []
        for x in range(3):
            nn = input('Nombre: ')
            e = Empleado(nn)  # instancia de la clase Empleado dentro de la clase Empresa
            self.lista.append(e)

    def listarEmpleados(self):
        return self.lista


empresa = Empresa()
for i in empresa.listarEmpleados():
    print(i.getNombre())