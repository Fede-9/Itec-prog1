# METODO CONSTRUCTOR
# Modificar un atributo

class Email():
    def __init__(self):
        self.enviado = False
        
    def enviarCorreo(self):
        self.enviado = True

miCorreo = Email()
print(miCorreo.enviado)
miCorreo.enviarCorreo()
print(miCorreo.enviado)