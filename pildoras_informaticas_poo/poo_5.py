# HERENCIA MULTIMPLE / METODO SUPER Y METODO INSTANCE 

class Vehiculos():
    def __init__(self,marca,modelo):  # pongo los atributos en comun
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False # estos atributos ya tienen designado un valor
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enMarcha}\nAcelera: {self.acelera}\nFrena: {self.frena}')


class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado = cargar
        if (self.cargado):
            return 'La furgoneta esta cargada'
        else:
            return 'la furgoneta no esta cargada'




class Moto(Vehiculos):
    tirarWily = ''
    #con este metodo tiene en total 5 metodos
    def wily(self): #metodo propio de la clase Moto 
        self.tirarWily = 'Estoy tirando un wily'

    def estado(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enMarcha}\nAcelera: {self.acelera}\nFrena: {self.frena}\n{self.tirarWily}')




class VElectricos():  #vehiculos electricos
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


class BiciElectrica(VElectricos,Vehiculos): #se da preferencia ala clase que esta mas a la izquierda.
    pass


print('------- PRIMER OBJETO ---------')
miMoto = Moto('Honda','XR 125')
miMoto.wily()
miMoto.estado() #aca llamamos al metodo estado de la clase Moto porque siempre se sobreescribe el metodo que heredas de la clase padre. 


print('--------- SEGUNDO OBJETO ---------')
miFurgoneta = Furgoneta('Ford','Focus')
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

print('------ TERCER OBJETO -------')
miBici = BiciElectrica()