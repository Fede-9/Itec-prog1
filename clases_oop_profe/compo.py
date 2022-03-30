# Agregación y Composición. 
# Ambos conceptos tienen la misma implementación: la instanciación de una clase al interior de otra. 
# La diferencia tiene que ver con la necesidad de la existencia de los objetos. 
# Pero en términos prácticos funcionan de manera similar. 
# Por tanto, de ahora en más nos vamos a referir a esta operación solamente como composición.

class Puerta():
    def __init__(self, uv, uh):
        self.uv = uv
        self.uh = uh

    def abrirPuerta(self):
        print("Abierta la puerta", self.uv, self.uh)

    def cerrarPuerta(self):
        print("Cerrada la puerta", self.uv, self.uh)


class Auto():
    def __init__(self, tipoAuto):
        self.p1 = Puerta("delantera", "izquierda")
        self.p2 = Puerta("delantera", "derecha")
        if tipoAuto == "sedán":
            self.p3 = Puerta("trasera", "izquierda")
            self.p4 = Puerta("trasera", "derecha")

a1 = Auto('sedán') 
a1.p1.abrirPuerta()
a1.p4.cerrarPuerta()
a2 = Auto('cupé')
a2.p1.abrirPuerta()
a2.p2.cerrarPuerta()