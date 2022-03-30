# 3) Crea las siguientes clases (cada una en su archivo): 
#  Motor: con métodos para arrancar el motor y apagarlo. 
#  Rueda: con métodos para inflar la rueda y desinflarla. 
#  Ventana: con métodos para abrirla y cerrarla. 
#  Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta. 
#  Coche: con un motor, cuatro ruedas y dos puertas;  con los métodos que te parezcan 

class Motor():
    def __init__(self):
        self.encendido = True
    
    def arrancarMotor(self):
        if self.encendido == True:
            print('El motor ya está encendido')
        else:
            print('El motor esta apagado')
    
    def apagarMotor(self):
        if self.encendido == True:
            print('El motor ya se esta apagando')
        else:
            self.encendido = False


if __name__ == '__main__':
    auto1 = Motor()
    print(auto1.arrancarMotor())
    print(auto1.apagarMotor())
    