class Coche():
    #propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
    #comportamineto/metodo
   
    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if (self.enmarcha): # si enmarcha=True
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'
        

miCoche = Coche() #instanciamos la clase para crear el objeto

print(f'El largo del coche es: {miCoche.largoChasis}')
print(f'El coche tiene: {miCoche.ruedas} ruedas')
miCoche.arrancar()  #lo arranco
print(miCoche.estado())


print('------------- A continuacion creamos el segundo objeto --------- ')

miCoche2 = Coche()

print(f'El largo del coche es: {miCoche2.largoChasis}')
print(f'El coche tiene: {miCoche2.ruedas} ruedas')
print(miCoche2.estado())
