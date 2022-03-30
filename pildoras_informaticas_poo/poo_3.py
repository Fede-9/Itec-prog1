#encampsulacion de metodos
class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 
        self.__enmarcha = False # a este atrivuto solo lo podemos modificar con el metodo arrancar

    
   
    def arrancar(self,arrancamos): 
        self.__enmarcha = arrancamos
        
        if (self.__enmarcha): # si es True llama al metodo y almacena lo que retorna el metodo chequeoInterno en la variable chequeo
            chequeo = self.__chequeoInterno()


        if (self.__enmarcha and chequeo): 
            return 'El coche esta en marcha'
        
        elif (self.__enmarcha and chequeo==False):
            return 'Hay algo mal en el chequeo.. No podemos arrancar'

        else:
            return 'El coche esta parado'
    

    def estado(self): 
        print(f'El coche tiene: {self.__ruedas}\nUn ancho de: {self.__anchoChasis}\nUn largo de: {self.__largoChasis}')

    
    def __chequeoInterno(self): #metodo encapsulado
        print('Realizando chequeo interno...')

        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if (self.gasolina == 'ok') and (self.aceite == 'ok') and (self.puertas == 'cerradas'):
            return True
        else:
            return False
    
                    
                    
        

miCoche = Coche() 

print(miCoche.arrancar(True))  
miCoche.estado()




print('------------- A continuacion creamos el segundo objeto --------- ')

miCoche2 = Coche()

print(miCoche2.arrancar(False))
miCoche2.estado()