# ------------------ ENCAPSULAMIENTO CON METODOS ---------------
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



    def mostrarDatos(self): # desde aca si podemos acceder ala propiedad o metodo encapsulado
        f'Nombre: {self.nombre} - Creditos: {self.creditos} - Imparticion: {self.__imparticion}'
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print('Existe docente asignado.')
        else:
            print('No existe docente asignado.')
            



    def __verificarDocente(self): # metodo encapsulado 
        #print('Verificando si existe docente asignado.....')
        if self.__imparticion == 'Presencial':
            return True
        else:
            return False



curso1 = Curso('Matematica',5,'Ingenieria civil')
print(curso1.nombre)
curso1.mostrarDatos()




# curso2 = Curso('Lenguaje',4,'Ingenieria industrial')
# print(curso2.nombre)