# ENCAPSULACION: es el ocultamiento de datos del estado interno para proteger la integridad del objeto.

class Cliente():
    def __init__(self):
        self.__codigo = 1234

    def __cuenta(self):
        print('cuenta de procesamiento')
    
    def getcodigo(self):
        return self.__codigo


persona = Cliente()
#objeto._nombre clase__nombre atributo
print(persona._Cliente__codigo) # lo printeo de pecho
persona._Cliente__cuenta() # es lo mismo que printearlo de pecho