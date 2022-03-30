# 3) Crea las siguientes clases (cada una en su archivo): 
#  Motor: con métodos para arrancar el motor y apagarlo. 
#  Rueda: con métodos para inflar la rueda y desinflarla. 
#  Ventana: con métodos para abrirla y cerrarla. 
#  Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta. 
#  Coche: con un motor, cuatro ruedas y dos puertas;  con los métodos que te parezcan 

class Ventana():
    def __init__(self):
        self.open = False
    
    def abrirVentana(self):
        if self.open == True:
            print('La ventana ya está abierta')
        else:
            self.open = True
    
    def cerrarVentana(self):
        if self.open == False:
            print('La ventana ya esta cerrada')
        else:
            self.open = False
    
    def getWindowState(self):
        return self.open


ventana1 = Ventana()
ventana1.abrirVentana()
ventana1.cerrarVentana()
ventana1.getWindowState()
