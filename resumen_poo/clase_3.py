# ------------ ENCAPSULAMIENTO ---------
class Curso():
#     nombre = 'Matematica'
#     creditos = 5
#     profesion = 'Ingenieria civil'

#estado inicial del objeto
    def __init__(self,nom,cre,pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = 'Presencial'  # propiedad encapsulada / no puede ser accesible desde afuera

    def mostrarDatos(self): # desde aca si podemos acceder ala propiedad encapsulada
        return f'Nombre: {self.nombre} - Creditos: {self.creditos} - Imparticion: {self.__imparticion}'



curso1 = Curso('Matematica',5,'Ingenieria civil')
print(curso1.nombre)
print(curso1.mostrarDatos()) 




# curso2 = Curso('Lenguaje',4,'Ingenieria industrial')
# print(curso2.nombre)