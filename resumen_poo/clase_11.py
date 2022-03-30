# -------- POLIMORFISMO ------- muchas formas de comportamiento
# tiene como finalidad que un objeto puede cambiar dependiendo del contexto del cual se utiliza

class Estudiante():

    def describir(self):
        print('Soy un buen estudiante...')


class Docente():

    def describir(self):
        print('Soy un buen docente...')
        

class Trabajador():

    def describir(self):
        print('Trabajo en una empresa')


def describirPersona(persona):
    persona.describir()



# def describirPersona(p1,p2,p3):   #tambien lo puedo hacer de esta manera
#     p1.describir()
#     p2.describir()
#     p3.describir()



doc1 = Estudiante()
doc2 = Docente()
doc3 = Trabajador()

doc1.describir()
doc2.describir()
doc3.describir()

describirPersona(doc1)
describirPersona(doc2)
describirPersona(doc3)

#describirPersona(doc1,doc2,doc3)