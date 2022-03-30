# 3) Crea las siguientes clases (cada una en su archivo): 
#  Motor: con métodos para arrancar el motor y apagarlo. 
#  Rueda: con métodos para inflar la rueda y desinflarla. 
#  Ventana: con métodos para abrirla y cerrarla. 
#  Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta. 
#  Coche: con un motor, cuatro ruedas y dos puertas;  con los métodos que te parezcan 

class Rueda():
    def __init__(self):
        self.condicionRueda = False

    def inflar(self):
        if self.condicionRueda == False:
            print('Inflando ruedaaa...')
            self.condicionRueda = True

    def desinflar(self):
        if self.condicionRueda == True:
            print('Desinflando ruedaa....')
            self.condicionRueda = False

if __name__ == '__main__':
    bici = Rueda()
    bici.inflar()
    bici.desinflar()