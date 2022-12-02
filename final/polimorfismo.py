class Perro():
    def hablar(self):
        print('soy el perro')

class Caniche():
    def hablar(self):
        print('soy el caniche')

class Dogo():
    def hablar(self):
        print('soy un dogo')


def hablando(objeto):
    objeto.hablar()



perro = Perro()
cani = Caniche()
dogo = Dogo()

hablando(perro)
hablando(cani)
hablando(dogo)
