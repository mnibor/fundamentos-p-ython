# OPERADORES DE COMPARACIÓN

a = 20
b = 15

# MENOR QUE Y MENOR O IGUAL QUE

result = a < b
print(f'Si a = {a} y b = {b}, la comprobación (a < b) es {result}')

# MAYOR QUE Y MAYOR O IGUAL QUE
print('******************** MAYOR QUE Y MAYOR O IGUAL QUE *****************')

result = a > b
print(f'Si a = {a} y b = {b}, la comprobación (a > b) es {result}')

# ES DISTINTO O NO IGUAL
print('******************** DISTINTO O NO IGUAL *****************')
a = 20
b = 20

result = a != b
print(f'Si a = {a} y b = {b}, la comprobación (a != b) es {result}')

# IGUAL A
a = 'Pepe'
b = 'Pepe'

result = a == b
print(f'Si a = {a} y b = {b}, la comprobación (a == b) es {result}')

# OPERADORES LOGICOS

# AND
a = True
b = True
result = a and b
print(f'Si a = {a} y b = {b}, la comprobación (a and b) es {result}')

a = True
b = False
result = a and b
print(f'Si a = {a} y b = {b}, la comprobación (a and b) es {result}')

a = False
b = True
result = a and b
print(f'Si a = {a} y b = {b}, la comprobación (a and b) es {result}')

a = False
b = False
result = a and b
print(f'Si a = {a} y b = {b}, la comprobación (a and b) es {result}')

# OR
a = True
b = True
result = a or b
print(f'Si a = {a} y b = {b}, la comprobación (a or b) es {result}')

a = True
b = False
result = a or b
print(f'Si a = {a} y b = {b}, la comprobación (a or b) es {result}')

a = False
b = True
result = a or b
print(f'Si a = {a} y b = {b}, la comprobación (a or b) es {result}')

a = False
b = False
result = a or b
print(f'Si a = {a} y b = {b}, la comprobación (a or b) es {result}')

# NOT
a = True
result = not a
print(f'Si a = {a}, la comprobación (not a) es {result}')

a = False
result = not a
print(f'Si a = {a}, la comprobación (not a) es {result}')