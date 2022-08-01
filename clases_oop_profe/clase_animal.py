class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def speak(self):
        print("No sé como hablar")


class Gato(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age) # ejecuta el constructor de la clase madre

    def speak(self): # polimorfismo, sobreescribe el método de la clase madre
        print("Miauuu")


class Perro(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def speak(self):
        print("Guauuu")


if __name__ == "__main__":
    gato = Gato("Tom", 3)
    perro = Perro("Lassie", 2)
    animal = Animal('federico',23)

    print("Nombre:", gato.getName())
    print("Edad:", gato.getAge())
    gato.speak()

    print("Nombre:", perro.getName())
    print("Edad:", perro.getAge())
    perro.speak()

    print('Nombre: ',animal.getName())
    print('Edad: ',animal.getAge())
    animal.speak()