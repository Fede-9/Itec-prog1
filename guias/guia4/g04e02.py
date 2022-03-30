#Transformar la cadena "Curso de Python" en la cadena "Curso de Programación en Python".
#Cortar la cadena original, agregarle el literal "Programación en" y concatenar.

cadena = "Curso de Python"
x = cadena[:8]
x += " Programacion en Python"
print(x)

# otra forma de hacerlo

texto = "Curso de {} {} Python"
texto1 = texto.format("Programacion","en")
print(texto1)

#otra forma

cadena1 = 'Curso de Python'
lista = cadena1.split()
lista.insert(2,'Programacion')
lista.insert(3,'en')
#print(lista)
cadena_completa = ' '.join(lista)    
print(cadena_completa)  