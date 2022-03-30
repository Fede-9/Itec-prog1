from dataclasses import dataclass 
from typing import Any # cuando no queremos definir un tipo de dato concreto

@dataclass  #decorador nos permite crear clases que tengan muchos atributos y asi poder ahorrar codigo
class User():
    username : str
    email : str
    password : Any = 'Dato por default'


    def saludar(self):
        print(f'Hola mundo, te saluda el usuario {self.username}')



class Admin(User):  # hereda atributos y metodos
    pass
    
# class User():
#     def __init__(self,username,email):
#         self.username = username
#         self.email = email

if __name__ == '__main__':
    usuario = Admin('Federico','fedecometto@gmail.com')
    usuario.password = 'njsnjsndjjnd' # le puedo agregar un valor cuando quiera

    print(usuario.username)
    print(usuario.email)
    usuario.saludar()
    print(usuario.password)