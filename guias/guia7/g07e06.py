# 6) Hacer una clase Persona con dos métodos: uno para saber si es mayor de edad y el otro para 
# determinar si es varón o mujer.
#  En el programa principal instanciarlo, tomar nombre, edad y sexo, y finalmente mostrar 
# un cartel que diga por ejemplo ‘Juan es mayor de edad y es varón’.




class Persona():

    def __init__(self):
        self.nombre = input('Nombre: ')
        self.edad = int(input('Edad: '))
        self.sexo = input('Sexo (M/F): ')

    def mayorEdad(self):
        if self.edad >= 18:
            retorno = 'mayor'
        else:
            retorno = 'menor'
        return retorno

    def determinarSexo(self):
        if self.sexo.upper() == 'M':
            retorno = 'varon'
        else:
            retorno = 'mujer'
        return retorno 


if __name__ == "__main__":
    persona1 = Persona()
    persona2 = Persona()
    print(f'{persona1.nombre} es {persona1.mayorEdad()} y {persona1.determinarSexo()}')
    print(f'{persona2.nombre} es {persona2.mayorEdad()} y {persona2.determinarSexo()}')
    

# REALIZADO POR EL PROFE
  
class Persona():
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    
    def mayor(self):
        return self.edad >= 18

    def varonOmujer(self):
        if self.sexo == 'f':
            retorno = 'mujer'
        else:
            retorno = 'varon'
        return retorno



persona1 = Persona('fede',23,'f')
print(persona1.mayor())
print(persona1.varonOmujer())

