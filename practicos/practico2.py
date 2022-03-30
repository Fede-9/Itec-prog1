# ESTO ESTA ECHO POR EL PROFE (REVISAR PARA ENTENDERLO)

b2008 = 'Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f'

varones2018 = [[0, '@'], [19837,'Liam'], [18267,'Noah'], [14516, 'Michael'], 
[13525, 'James'], [13389, 'Oliver']]
nenas2018 = [[0, '@'], [18688, 'Emma'], [17921, 'Olivia'], [14924, 'Ava'], 
[14464, 'Isabella'], [13928, 'Sophia']]

def strAlistas():
    var2008 = []
    nen2008 = []
    b = b2008.split(',')
    for x in range(2, len(b), 3):
        if b[x] == 'm':
            var2008.append([int(b[x-1]), b[x-2]])
        else:
            nen2008.append([int(b[x-1]), b[x-2]])
    var2008.sort(reverse=True)
    nen2008.sort(reverse=True)
    var2008.insert(0, [0, '*'])
    nen2008.insert(0, [0, '*'])
    return var2008, nen2008

varones2008, nenas2008 = strAlistas()
print(varones2008)

def aps(a, p, s):
    if a == 2008:
        if s == 'f':
            n = nenas2008[p][1]
            c = nenas2008[p][0]
        else:
            n = varones2008[p][1]
            c = varones2008[p][0]
    else:
        if s == 'f':
            n = nenas2018[p][1]
            c = nenas2018[p][0]
        else:
            n = varones2018[p][1]
            c = varones2018[p][0]
    return n, c

def nombre(n, a):
    encontrado = False
    if a == 2008:
        for e in varones2008:
            if e[1] == n:
                encontrado = True
        for e in nenas2008:
            if e[1] == n:
                encontrado = True
    else:
        for e in varones2018:
            if e[1] == n:
                encontrado = True
        for e in nenas2018:
            if e[1] == n:
                encontrado = True
    return encontrado

# punto 1
n1, c1 = aps(2008, 2, 'f')
n2, c2 = aps(2018, 2, 'f')
dif = c1 - c2
if dif < 0:
    print(n2, 'mayor que', n1, 'por', dif*-1)
else:
    print(n1, 'mayor que', n2, 'por', dif)

# punto 2
for x in range(6):
    if varones2008[x][1][0] == 'J':
        print(varones2008[x][1])
    if nenas2008[x][1][0] == 'J':
        print(nenas2008[x][1])
    if varones2018[x][1][0] == 'J':
        print(varones2018[x][1])
    if nenas2018[x][1][0] == 'J':
        print(nenas2018[x][1])

# punto 3
print('---------------------------')
for e in varones2008:
    if nombre(e[1], 2018):
        print(e[1])
for e in nenas2008:
    if nombre(e[1], 2018):
        print(e[1])
