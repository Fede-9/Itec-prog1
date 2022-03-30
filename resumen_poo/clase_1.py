class Persona():
    # propiedades, caracteristicas o atributos
    apellidos = ''
    nombres = ''
    edad = 0
    despierta = False #persona dormida

    #funcionalidades
    def despertar(self):
        #self: parametro que hace referencia a la instancia perteneciente a la clase
        self.despierta = True #persona despierta
        print('Buen diaa')



persona1 = Persona()
persona1.apellidos = 'Cometto'
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)

persona2 = Persona()
persona2.apellidos = 'Villarino'
print(persona2.apellidos)
#persona2.despertar()
print(persona2.despierta)
