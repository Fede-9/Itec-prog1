class Perro():
    def hablar(self):
        print('soy el perro')

class Dogo():
    def hablar(self):
        print('soy un dogo')

class Caniche():
    def hablar(self):
        print('soy un caniche')

def hablando(objeto):
    objeto.hablar()


perro = Perro()
dogo = Dogo()
caniche = Caniche()

hablando(perro)
hablando(dogo)
hablando(caniche)