# Polimorfismo: el objeto puede cambiar de muchas formas.

class Coche():

    def desplazamiento(self):
        print('Me desplazo utilizando cuatro ruedas')


class Moto():

    def desplazamiento(self):
        print('Me desplazo utilizando dos ruedas')


class Camion():

    def desplazamiento(self):
        print('Me desplazo utilizando seis ruedas')



def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


# POLIMORFISMO

miVehiculo = Coche() 
#miVehiculo = Camion() 
#miVehiculo = Moto() 
desplazamientoVehiculo(miVehiculo)



# ------- SERIA MUCHO CODIGO HACERLO DE ESTA FORMA -------

# miVehiculo = Moto()
# miVehiculo.desplazamiento()

# miVehiculo2 = Coche()
# miVehiculo2.desplazamiento()

# miVehiculo3 = Camion()
# miVehiculo3.desplazamiento()

