# POLIMORFISMO CON METODOS

class Colombia():
    def capital(self):
        print('Bogota')
    
    def idioma(self):
        print('español')

class Francia():
    def capital(self):
        print('Paris')
    
    def idioma(self):
        print('frances')

colombiano = Colombia()
frances = Francia()

for pais in (colombiano,frances):
    pais.capital()
    pais.idioma()