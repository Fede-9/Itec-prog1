class Libro():
    def __init__(self,titulo,precio,autor=None):
        self.titulo = titulo
        self.precio = precio
        self.autor = autor
        self.capitulos = []
    
    def agregarCapitulo(self,capitulo):
        self.capitulos.append(capitulo)

    def totalPaginas(self):
        resultado = 0
        for capitulo in self.capitulos:
            resultado += capitulo.paginas
        return resultado

class Autor():
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Capitulo():
    def __init__(self,nombre,paginas):
        self.nombre = nombre
        self.paginas = paginas


autor1 = Autor('Federico','Cometto')
libro1 = Libro('Teoria python',450,autor1)
libro1.agregarCapitulo(Capitulo('Variables',155))
libro1.agregarCapitulo(Capitulo('Funciones',20))

print(libro1.titulo)
print(libro1.autor)
print(libro1.totalPaginas())







