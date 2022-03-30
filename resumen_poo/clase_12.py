# --- RELACIONES ENTRE CLASES -----  DEPENDENCIA/INDEPENDENCIA

class Pais():
    def __init__(self,nom,pre):
        self.nombre = nom
        self.presidente = pre

    def __str__(self):
        return f'Pais: {self.nombre} - Presidente: {self.presidente}' 
        

class Ciudad():
    def __init__(self,nom,hab,pai):
        self.nombre = nom
        self.habitantes = hab
        self.pais = pai

    def __str__(self):
        return f'Ciudad: {self.nombre} - Nº habitantes: {self.habitantes} - {self.pais}'

class Urbanizacion():
    def __init__(self,nom,ciu):
        self.nombre = nom
        self.ciudad = ciu

    def __str__(self):
        return f'Urbanizacion: {self.nombre} - {self.ciudad}'



pais1 = Pais('Argentina','Alberto')
print(pais1)

ciudad1 = Ciudad('Serrano',5000,pais1) 
print(ciudad1)

urba1 = Urbanizacion('La quinta',ciudad1)
print(urba1)
