# Operadores Logicos
# AND
# OR
# NOT

condicion_1 = 5 > 2
condicion_2 = 10 > 5

print(condicion_1 and condicion_2) # True and True ----> TRUE

print('-------------')
condicion_3 = 50 < 10

print(condicion_1 and condicion_3) # True and False ----> FALSE

# False and False ----> FALSE


# OR
print('----------- OR ---------------------')

condicion_1 = 5 > 2 # True
condicion_2 = 10 > 5 # True

condicion_3 = 50 < 10 # False
condicion_4 = 10 > 500 # False
print(condicion_1 or condicion_2) # True or True ----> TRUE

print(condicion_1 or condicion_3) # True or False ----> TRUE

print(condicion_3 or condicion_4) # False or False ----> FALSE

# NOT
print('------- NOT -----------------')
print(condicion_1) # True
print(not condicion_1) # not True ----> False

print('---condicion 4 ------')
print(condicion_4) # False
print(not condicion_4) # not False -----> True 