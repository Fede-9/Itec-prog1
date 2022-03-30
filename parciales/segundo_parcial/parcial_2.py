stock = open("stock_muebles.csv",'r')
lineas = stock.readlines()
lineas.pop(0)
stock.close()
todo = []
for e in lineas:
    lista = e.split(',')
    orden = lista[:3]
    
    

class Mueble():
    def __init__(self,cantidad,precio):
        self.precio = cantidad
        self.precio = precio
    
    def agregarMueble(self):
        pass


class Sillas(Mueble):
    def __init__(self,altas,bajas,cantidad,precio):
        Mueble.__init__(self,cantidad,precio)
        self.altas = altas
        self.bajas = bajas
    
    def agregarSilla(self,cantidad):
        self.cantidad = cantidad
    
    def mostrarSilla(self):
        pass
        


class Mesas(Mueble):
    def __init__(self,cuadradas,rectangulares,cantidad,precio):
        Mueble.__init__(self,cantidad,precio)
        self.cuadradas = cuadradas
        self.rectangulares = rectangulares
    
    def agregarMesa(self,cantidad):
        self.cantidad = cantidad
        

class Banquetas(Mueble):
    def __init__(self,fijas,regulables,cantidad,precio):
        Mueble.__init__(self,cantidad,precio)
        self.fijas = fijas
        self.regulables = regulables
    
    def agregarBanqueta(self,cantidad):
        self.cantidad = cantidad
        


