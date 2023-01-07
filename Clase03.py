# Tipos de Datos Numéricos

myIntegerNumber = 32
myFloatNumber = 65.5
print('Mi variable myIntegerNumber es:', type(myIntegerNumber))
print('Mi variable myFloatNumber es:', type(myFloatNumber))

# Tipos de Datos cadena
myStringValue = 'Es una prueba'
print('Mi variable myStringValue es:', type(myStringValue))

myValue: str = 'Mi valor cadena'
print(myValue)

myName = 'Pepe'
myLastname = 'Rodríguez'
# print('Mi nombre y Apellido son: ' + myName + ' ' + myLastname)
print('Mi Nombre y Apellido son:', myName, myLastname)
print(myName, 'llamá a', myLastname)

myAge = 32
print('Mi variable myAge es:', type(int(myAge)))
print('###################################################')
print('Mi Nombre y Apellido son:', myName, myLastname, 'y tengo', myAge, 'años')

# Tipos de datos booleanos - lógicos

myBooleanValue1 = True
myBooleanValue2 = False
print('###################################################')
print('Mi variable myBooleanValue1 es:', type(myBooleanValue1))
print('Mi variable myBooleanValue2 es:', type(myBooleanValue2))

myExpression = 3 > 5
print('Mi variable myExpression es:', type(myExpression), myExpression)

# Si A es verdadero
# Entonces tengo que decir que A es verdadero
# Caso contrario, tengo que decir que A es falso

# if myExpression == True:
#     print('La expresión myExpression es verdadera')
# else:
#     print('La expresión myExpression es falsa')

if myExpression:
    print('La expresión myExpression es verdadera')
else:
    print('La expresión myExpression es falsa')

# La función INPUT para ingresar datos desde la consola
print('###################################################')
print('###################################################')

myName = input('Ingrese su nombre: ')
myAge = input('Ingrese su edad: ')
print(myName, 'tiene', myAge, 'años')
# print(type(myName))

# Ejercicio: Tenemos un rectángulo, y se va a pedir que el operador ingrese el valor del lado mayor en cm, y el valor del lado menor, en cm y habrá que calcular el perímetro en cm y el área en cm2
# Tip: el perímetro es la suma de los cuatro lados
# Tip: el área es la multiplicación de los lados (*)
print('###################################################')
print('###################################################')

A = float(input('Ingrese el valor del lado mayor (en cm): '))
B = float(input('Ingrese el valor del lado menor (en cm): '))
perimetro = A + A + B + B
area = A * B
print('El perímetro del rectángulo es de: ', perimetro, 'cms')
print('El área del rectángulo es de: ', area, 'cm2')

