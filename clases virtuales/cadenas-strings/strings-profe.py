s = "Hola Juan, como estás?" # ['H', 'o', 'l', etcetera]

n = s.find('Juan')
print(s.find('Juan'))
m = s.find("Pepe")
o = s.find('n, c')

print('-----------------------')
letraO = s.find('o', 2)
print(n, m, o, letraO)

f = '12/05/1987'
print(f.split('/'))
l = s.split()
ll = s.split(',')
print(l, ll)
print(s.upper())

print(s[5])
for i in range(len(s)):
    if s[i] == ',':
        print('encontré una coma en la posición', i)

s = "Hola Juan, como estás?"
principio = s[:4]
nombre = s[5:9]
fin = s[-1:]

print(principio)
print(nombre)
print(fin)

""" 
for i in range(len(s)):
    print(s[-1-i])
"""
# leng = (len(s) * (-1)) - 1
# for i in range(-1, leng, -1):
#     print(s[i])
