from os import kill
from fuimba import *  

class Fabrica():
    def __init__(self,muebles,tipos,precios):
        self.muebles = muebles
        self.tipos = tipos
        self.precios = precios

class Productos(Fabrica):
    def addMuebles (self):#agregar nuevo mueble
        self.newMueble = input('Ingrese nuevo mueble: ')
        self.muebles.append(self.newMueble)        
        self.newTipo = input('Que tipo de mueble es: ')
        self.tipos.append(self.newTipo)
        self.newPrecio= inputInt('Ingrese precio del mueble: ')
        self.precios.append(self.newPrecio)

    def artiPprecio (self):#consultar stock por precio ingresado
        self.consPrecio = inputInt('Ingrese precio a consultar: ')
        for buscar in range(len(self.precios)):
            if self.precios[buscar] > self.consPrecio :
                print(f'Art Nº {buscar} > Muebles: {self.muebles[buscar]} - Tipo: {self.tipos[buscar]} - Precio: ${self.precios[buscar]}.')


    def cantMueblesPorTipo(self):#muebles por tipo
        self.stockPorTipo1 = {}
        self.stockPorTipo2 = {}       
        for e in range(len(self.tipos)):
            mueble = self.muebles[e]           
            tipo = self.tipos[e]
            if mueble not in self.stockPorTipo1.keys():
                self.stockPorTipo1[mueble] = [tipo,1]        
            else:  
                if tipo == self.stockPorTipo1[mueble][0]:     
                    self.stockPorTipo1[mueble][1] += 1
                else:
                    if mueble not in self.stockPorTipo2.keys():
                        self.stockPorTipo2[mueble] = [tipo,1]        
                    else:      
                        self.stockPorTipo2[mueble][1] += 1
                    
        for k,v in self.stockPorTipo1.items():
            print(f'Mueble: {k} - Tipo: {v[0]} - Cantidad: {v[1]}') 
        for ke,va in self.stockPorTipo2.items():
            print(f'Mueble: {ke} - Tipo: {va[0]} - Cantidad: {va[1]}') 
        
  
class App():
    def __init__(self):
        empresa = Productos(mueblesStock,tipos,precios)
        entrada = True
        while entrada:
            subrayar()
            print('   > Menu Principal <')
            makeMenu(uno='Añadir nuevo Mueble.',dos='Consultar stock por precio.',tres='Contar la cantidad de cada mueble discriminado por tipo.')
            print('0 > Salir.')
            subrayar()
            opMenu = valInt('- Ingrese opcion: ',min= -1,max=4)
            if opMenu ==1:
                empresa.addMuebles()
                print('> Mueble añadido con exito <')
                backTomenu()
            elif opMenu ==2:
                print('> Se muestran resultados de la busqueda <')
                empresa.artiPprecio()
                backTomenu()
            elif opMenu ==3:
                print('> Cantidad de muebles por tipo <')
                empresa.cantMueblesPorTipo()
                backTomenu()
            elif opMenu ==0:
                print('Esta seguro que desea salir?')
                print('1= Si | 2=No')
                salir = valInt('Ingrese opcion: ',min=0,max=3)
                entrada = False        


if __name__=='__main__':
    stockInicial = open('stock_muebles.csv','r')
    leoStock = stockInicial.readlines()
    leoStock.pop(0)
    mueblesStock= []
    tipos = []
    precios = []
    stockInicial.close()
    for e in leoStock:
        lis = e.split('\n')
        lis.pop(1)
        for x in lis:
            separo = x.split(',')
            mueblesStock.append(separo[0])           
            tipos.append(separo[1])
            precios.append(int(separo[2]))
    a = App()    
    