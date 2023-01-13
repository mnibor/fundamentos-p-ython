'''
EJERCICIO INTEGRADOR DE MULTIPLICACION Y DIVISION
Calcular el área de un triángulo rectángulo
Pedir al operador que ingrese la base del triángulo
Pedir al operador que ingrese la altura del triángulo
Mostrar el resultado del área
* considerar la posibilidad que el operador ingrese decimales.
'''

ba = float(input('Ingrese la base del triángulo rectángulo (cms): '))
h = float(input('Ingrese la altura del triángulo rectángulo (cms): '))

sup = (ba * h) / 2

print(f'Dado el triángulo rectángulo de base = {ba} [cm] y altura = {h} [cm], su superficie es: {sup} cm2 ')