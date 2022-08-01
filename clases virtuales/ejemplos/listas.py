#(4 de la guía 2) Pedir el ingreso de 10 números. Contar los mayores de 23.
#Almacenar los que cumplen la condición.  Mostrar los resultados.



#lista = ["hola",2.3,3]


#for x in range(len(lista)):                  FORMA TRADICIONAL DE RECORRER UNA LISTA
 #   print(lista[x])




#for x in lista:                             OTRA FORMA DE RECORRER UNA LISTA
 #   print(x)



#lista = []                                  CON EL APPEND AGREGO AL ULTIMO EN LA LISTA
#lista.append("hola")
#lista.append(15)
#lista.append(1.2)
#print(lista)



#n = []
#for x in range(5):                        X VA TOMANDO LOS VALORES Y VA MULTIPLICANDO POR 2 Y LOS VA AGREGANDO A LA LISTA
#    n.append(x * 2)
#print(n) 


# n = []                                #    VA AGREGANDO UN NOMBRE EN CADA VUELTA
# for x in range(3):                    
#     nombre = input("ingrese su nombre: ")                       
#     n.append(nombre)
# print(n)

# for i in range(3):                    # EN ESTE FOR UTILIZO EL SUBINDICE 
#     print(n[i])


#lista = [23,58,96]                   ACA REEMPLAZO UN ELEMENTO DE LA LISTA
#lista[1] = 100
#print(lista)

# lista = [23,58,98]                   #CON EL INSERT AREGO ELEMENTOS A LA LISTA EN LA UBICACION QUE YO QUIERO
# lista.insert(1,100)
# print(lista)


#lista = [23,58,98]                   
#lista.insert(1,100)
#print(lista)

#x = lista.pop()                        #EL 'POP' SIN NINGUN PARAMETRO SACO EL ULTIMO ELEMENTO DE LA LISTA Y LO PUEDO ALMACENAR EN UNA VARIABLE
#print(lista,x)

#z = lista.pop(1)                      #EN ESTE CASO LE DIGO LA POSICION DE QUE ELEMENTO SACAR
#print(lista,Z)

#x = lista.pop()                       #ES LO MISMO LO UNICO QUE NO MUESTRO QUE ELEMTO ESTOY SACANDO
#print(lista)

#z = lista.pop(1)                      #ES LO MISMO LO UNICO QUE NO MUESTRO QUE ELEMTO ESTOY SACANDO
#print(lista)


#lista.insert(1,100)
#print(lista)

#lista = [23,58,98]                   #CON EL REMOVE LE DIGO QUE ELEMENTO QUIERO SACAR POR SU VALOR Y NO POR POSICION
#lista.remove(23)
#print(lista)

  
# persona1 = ['fede', 22]
# persona2 = ['papel', 21]
# lista = [persona1, persona2]     #CONCATENAR
# print(lista)

#vocales = ['E','I','O']
#vocales += ['U']
#print(vocales)

#vocales = ['A'] + vocales
#print(vocales)


#fecha = [27,'octubre',1997]
#fecha[2] = 1998                   #MODIFICAR CUALQUIER ELEMENTO DE LA LISTA
#print(fecha)



#a = 5
#b = a      # Hacemos una copia del valor de a
#print(a, b)

#a = 4     # de manera que aunque cambiemos el valor de a ...
          # ... b conserva el valor anterior de a en caso de necesitarlo
#print(a,b)

#RECORRER UNA LISTA

#letras = ["A", "B", "C"]
#for i in letras:          
#    print(i, end=' ')



#lista = ["A", "B", "C"]
#for x in range(len(lista)):
#    print(lista[x], end=" ")


#RECORRER UNA LISTA ALRREVES
#letras = ["A", "B", "C"]
#for i in range(len(letras)-1, -1, -1):
#    print(letras[i], end=" ")



#RECORRER Y MODIFICAR UNA LISTA
#letras = ['A','B','C']
#print(letras)
#for i in range(len(letras)):           
#  letras[i] = 'X'
#  print(letras)

#ELIMINAR VALORES DE UNA LISTA .... SIEMPRE HAY QUE RECORRERLA AL REVES
#letras = ["A", "B", "C"]
#print(letras)
#for i in range(len(letras)-1, -1, -1):
#    if letras[i] == "B":
#        del letras[i]
 #   print(letras)


#SABER SI UN VALOR ESTA O NO EN UNA LISTA
personas_autorizadas = ["Alberto", "Carmen"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
  print("Está autorizado")
else:
  print("No está autorizado")

#PARA SABER SI UN VALOR NO ESTA EN UNA LISTA
personas_autorizadas = ["Alberto", "Carmen"]
nombre = input("Dígame su nombre: ")
if nombre not in personas_autorizadas:
  print("No está autorizado")
else:
  print("Está autorizado")


