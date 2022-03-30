# FUNCIONES CON ATRIBUTOS

class Persona():
    edad = 27
    nombre = 'Federico'
    pais = 'Brasil'

doctor = Persona()
print('La edad es:', doctor.edad)
print('La edad es:', getattr(doctor,'edad'))
print('El doctor tiene una edad?', hasattr(doctor,'edad'))  # sirve para validar TRUE / FALSE
print('El doctor tiene una edad?', hasattr(doctor,'apellido'))
print('Antes era:',doctor.nombre)
setattr(doctor,'nombre','Tomas') # sirve para hacer cambio de valor 
print('Ahora se llama:',doctor.nombre)
delattr(Persona,'pais') # sirve para eliminar atributos
