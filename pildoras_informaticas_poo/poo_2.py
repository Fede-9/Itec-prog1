#encapsulacion de atributos
class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #encapsulo asi no es accesible desde el exterior pero si puedo acceder dentro de la clase
        self.__enmarcha = False

    
   
    def arrancar(self,arrancamos): # depende de lo que le pasemos por parametro
        self.__enmarcha = arrancamos
        if (self.__enmarcha): #evalua si self.enmarcha es True o False.
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'
    

    def estado(self): #este metodo solo nos informa
        print(f'El coche tiene: {self.__ruedas}\nUn ancho de: {self.__anchoChasis}\nUn largo de: {self.__largoChasis}')
    
                    
                    
        

miCoche = Coche() #instanciamos la clase para crear el objeto

print(miCoche.arrancar(True))  
miCoche.estado()



print('------------- A continuacion creamos el segundo objeto --------- ')

miCoche2 = Coche()
miCoche2.ruedas=2 #no puedo cambiar la propiedad porque esta encapsulada ya que no puede existir autos que no tengan 4 ruedas por ejemplo
print(miCoche2.arrancar(False))
miCoche2.estado()

