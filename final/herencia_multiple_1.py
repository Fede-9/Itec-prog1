class Telefono():
    def __init__(self):
        pass

    def llamar(self):
        print('llamando...')
    
    def ocupado(self):
        print('ocupado...')

class Camara():
    def __init__(self):
        pass

    def fotografia(self):
        print('tomando foto...')


class Reproducion():
    def __init__(self):
        pass

    def reproduccionMusica(self):
        print('reproduciendo musica...')

    def reproduccionVideo(self):
        print('reproducir video...')



class Smartphone(Telefono, Camara, Reproducion):
    def __del__(self):
        print('telefono apagado')



movil = Smartphone()


movil.llamar()
movil.ocupado()
movil.fotografia()
movil.reproduccionMusica()
movil.reproduccionVideo()