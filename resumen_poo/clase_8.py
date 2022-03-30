# ---------- SOBREESCRITURA - METODO SUPER() ---------

class Persona():
    def __init__(self,apePat,apeMat,nom):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nom

    def mostraNombreCompleto(self):
        return f'{self.apellidoPaterno} - {self.apellidoMaterno} - {self.nombres}'

    def datos(self):
        print(self.mostraNombreCompleto())

class Estudiante(Persona): #la clase estudiante hereda todo lo que tiene la clase persona.
    def __init__(self, apePat, apeMat, nom,pro): # la profesion es argumento propio de la clase hija.
        super().__init__(apePat, apeMat, nom)
        self.profesion = pro

    def datos(self): #sobreescribiendo metodo.
        super().datos()
        print(f'Profesion: {self.profesion}')
        

        
    

estu1 = Estudiante('Cometto','Tortu','Federico','Programador')
# print(estu1.mostraNombreCompleto())
# print(estu1.profesion)
estu1.datos()
    

