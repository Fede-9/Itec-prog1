# 4) Desarrolla una clase Cancion con los siguientes atributos: titulo y autor
# y los siguientes métodos: 
# constructor que recibe como parámetros el título y el autor de la canción (por este orden). 
# dameTitulo(): devuelve el título de la canción. 
# dameAutor(): devuelve el autor de la canción. 
#  ponerTitulo(String):  establece el título de la canción. 
#  ponerAutor(String): establece el autor de la canción. 

class Cancion():
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def dameTitulo(self):
        return f'Titulo de la cancion: {self.titulo}'

    def dameAutor(self):
        return self.autor

    def ponerTitulo(self,nuevoTitulo):
        self.titulo = nuevoTitulo
        return self.titulo
        
    def ponerAutor(self,nuevoAutor):
        self.autor = nuevoAutor
        return self.autor

if __name__ == '__main__':
    cliente = Cancion('Lo fragil de la locura','La Renga')
    print(cliente.dameTitulo())
    print(f'Autor: {cliente.dameAutor()}')
    print('Titulo de la nueva cancion: ',cliente.ponerTitulo('El pibe de los astilleros'))
    print('Autor: ',cliente.ponerAutor('Indio Solari'))