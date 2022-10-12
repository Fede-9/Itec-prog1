# -------------- METODO GET - SET ----- -----> sirven para modifcar propiedades dentro de una clase


class Cuenta():
    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

    # Getters (metodos GET)  ----> nos permiten obtener un valor
 
    def getSaldo(self):
        return self.__saldo

    def getPropietario(self):
        return self.__propietario

    def getMoneda(self):
        return self.__moneda


    # Setters (metodos SET) -----> nos permiten modificar un valor

    def setMoneda(self, moneda):  # nos permite modificar el valor de moneda
        self.__moneda = moneda




cuenta1 = Cuenta('Federico',15000,'pesos')
print(cuenta1.getSaldo())
print(cuenta1.getMoneda()) 
cuenta1.setMoneda('Dolares') #hago el cambio de moneda
print(cuenta1.getMoneda())


