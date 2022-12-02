# En el ejemplo a continuación vemos el mismo nombre de Método en diferentes clases. 
# Al momento de crear una instancia y llamar al método vemos que aunque se llamen igual 
# el interprete se guía por el nombre de la clase.

class Marino(): #Clase Padre
    def hablar(self): #Método Hablar
        print("Hola soy marino ...")

class Pulpo(Marino): #Clase Hija
    def hablar(self): #Método Hablar
        print("Soy un Pulpo")
        

class Foca(Marino): #Clase Hija
    def hablar (self, mensaje): #Método Hablar
        print (mensaje)

marino = Marino() #instancia
pulpo = Pulpo() #Instancia
foca = Foca() #Instancia


marino.hablar()#llamamos al metodo
pulpo.hablar() #Llamamos al método
foca.hablar("Soy una foca, este es mi mensaje") #Llamamos al método



# Como podemos ver en el ejemplo el nombre de método es el mismo, cuando lo llamamos Python sabe 
# cual ejecutar porque se lo dice la clase a la que pertenece el objeto 
# (en ese caso pulpito, pertenece a la clase “pulpo” por ende obviamente llamará al método 
# hablar de dicha clase y no de ninguna otra.).


