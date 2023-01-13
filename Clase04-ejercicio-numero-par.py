'''
Verificar si un número ingresado por el operador, es par o impar
Tip - Un número es par si el módulo de ese número con respecto al 2, da cero
'''

value = int(input('Ingrese un número entero: '))
result = value % 2

if result == 0:
    print(f'El número ingresado por el operador es el {value} ES UN NÚMERO PAR')
else:
    print(f'El número ingresado por el operador es el {value} ES UN NÚMERO IMPAR')