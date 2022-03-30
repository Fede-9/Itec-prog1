# 3) Crea las siguientes clases (cada una en su archivo): 
#  Motor: con métodos para arrancar el motor y apagarlo. 
#  Rueda: con métodos para inflar la rueda y desinflarla. 
#  Ventana: con métodos para abrirla y cerrarla. 
#  Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta. 
#  Coche: con un motor, cuatro ruedas y dos puertas;  con los métodos que te parezcan 

from ventana import Ventana

class Puerta(Ventana):
    def __init__(self):
        super().__init__()
        self.abierta = False
    
    def abrirPuerta(self):
        if self.abierta:
            print('La puerta ya esta abierta')
        else:
            self.abierta = True

    def cerrarPuerta(self):
        if not self.abierta:
            print('La puerta ya esta cerrada')
        else:
            self.abierta = False
            
            
    def getClosedOpen(self):
        return self.abierta

if __name__ == '__main__':
    puerta1 = Puerta()