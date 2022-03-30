# 10) Definir una clase Telefono, sus atributos son: marca, modelo, sistema operativo, plan(costo) y 
# cantidad de RAM. 
# Sus métodos son: costo anual, mostrar Sistema Operativo y si es gama alta o no (con 6 o más gigas de RAM) .

class Telefono():
    def __init__(self,marca,modelo,sistemaOperativo,plan,ram):
        self.marca = marca
        self.modelo = modelo
        self.sistemaOperativo = sistemaOperativo
        self.plan = plan
        self.ram = ram

    def costoAnual(self):
        return self.plan * 12

    def sistemaOp(self):
        return self.sistemaOperativo

    def gama(self):
        if self.ram >= 6:
            retorno = 'Alta'
        else:
            retorno = 'Baja'
        return retorno

if __name__ == "__main__":
    cliente = Telefono('Samsung','MotoG','Android',1000,8)
    print(f' Costo Anual: {cliente.costoAnual()}\n Sitema Operativo: {cliente.sistemaOp()}\n Tipo de gama: {cliente.gama()}')
