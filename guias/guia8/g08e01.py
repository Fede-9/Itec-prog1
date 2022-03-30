# 1) Crea una clase Cuenta (bancaria) con atributos para el número de cuenta, el DNI del cliente, el saldo actual y el interés
#  anual que se aplica a la cuenta (porcentaje). Define en la clase los siguientes métodos: constructor con DNI, saldo e interés. 
# Método actualizarSaldo(): actualizará el saldo de la cuenta aplicándole el interés diario (interés anual dividido entre 365 aplicado 
# al saldo actual), método ingresar(float):  permitirá ingresar una cantidad en la cuenta, método retirar(float): permitirá sacar una 
# cantidad de la cuenta (si hay saldo). Finalmente, un método que nos permita mostrar todos los datos de la cuenta. 


# from validacion_entero import validacionFloat

class Cuenta():
    def __init__(self,numeroCuenta,dni, saldo,interesAnual):
        self.numeroCuenta = numeroCuenta
        self.dni = dni
        self.saldo = saldo
        self.interesAnual = interesAnual

    def actualizarSaldo(self):
        self.saldo = self.saldo + self.saldo * (self.interesAnual / 365)

    def ingresar(self):
        try:
            dinero = float(input('Coloque el monto a ingresar: '))
        except:
            return f'Error'
        else:
            self.saldo += dinero
            return f'Ingreso {dinero} pesos a su cuenta'

    def retirar(self):
        try:
            dinero = float(input('Coloque el monto a retirar: '))
        except:
            return f'Error'
        else:
            if self.saldo > dinero:
                self.saldo -= dinero
                return f'Retiro {dinero} pesos'
            else:
                return f'No existe esa cantidad disponible'  

    def getAccount(self):
        print(f'Numero de cuenta: {self.numeroCuenta}')
        print(f'DNI: {self.dni}')
        print(f'Saldo: {self.saldo}')
        print(f'Interes anual: {self.interesAnual}')



if __name__ == '__main__':
    miCuenta = Cuenta(123, 41964743,344500.50,20)
    miCuenta.getAccount()
    miCuenta.actualizarSaldo()
    #print(miCuenta.ingresar())
    miCuenta.getAccount()  