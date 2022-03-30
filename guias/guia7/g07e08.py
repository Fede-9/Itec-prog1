# 8) Heredar de la clase Auto una clase Marca, que agregue el atributo Modelo. 
# Instanciar en  el programa principal (una sola línea en total). 
# La salida debe ser por ejemplo: Auto: VW Modelo: Gol

from g07e07 import Auto

#ES LO MISMO !!!

# class Auto():
#     def __init__(self, marca, año):
#         self.marca = marca
#         self.año = año

class Marca(Auto):
    def modelando(self,modelo):
        self.modelo = modelo
        
if __name__ == "__main__":
    auto1 = Marca('Ford',2021)
    auto1.modelando('Focus')
    print(f' Auto: {auto1.marca}\n Modelo: {auto1.modelo}')