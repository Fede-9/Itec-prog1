#1) Hacer una clase Teléfono con los atributos marca, modelo y costo mensual y un método que 
# muestre (o devuelva) el costo anual.

class Telefono():
    def __init__(self,marca,modelo,costo):
        self.marca = marca
        self.modelo = modelo
        self.costo = costo

    def costoAnual(self):
        total = self.costo * 12
        return f'Su costo anual es de: {total}'

if __name__ == '__main__':
    cliente1 = Telefono('samsung','motoG', 950)
    print(cliente1.costoAnual())
    cliente2 = Telefono('samsung','motoG', 500)
    print(cliente2.costoAnual())


    print(cliente1.marca)
    print(cliente2.marca)

    for cliente in cliente1,cliente2:
        print(cliente.modelo)
        print(cliente.costo)