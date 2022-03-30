g = open('pelis.csv')
todo = g.readlines()
g.close()
todo.pop(0)
acum = 0
for fila in todo:
    li = fila.split(',')
    acum += int(li[3])
   
print(acum)