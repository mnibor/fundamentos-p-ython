'''
Pedir al operador que ingrese un número mayor que cero.
1.- hacer una comprobación de ese número y lanzar un mensaje del tipo: "el numero ingresado está entre 0 y 10". Caso contrario decir que el número es mayor que 10 o menor que cero,
'''

value = float(input('Ingrese un número: '))

if (value >= 0) and (value <= 10):
	print(f'El número ingresado es el {value} y se encuentra en el rango de 0 - 10 ')
elif value > 10:
	print(f'El número ingresado es el {value} y es mayor que 10 ')
else:
	print(f'El número ingresado es el {value} y es menor que 0 ')

# Si el numero ingresado esta entre 0 y 10 o si el número ingresado es un par: ponemos el mensaje "el número es correcto"

print('')
print('')

if ((value >= 0) and (value <= 10)) or (value % 2 == 0):
	print(f'El número ingresado {value} ES UN NÚMERO CORRECTO')
else:
	print(f'El número ingresado {value} ES UN NÚMERO INCORRECTO')

print('')
print('')

if not (value % 2 == 0):
	print(f'El número ingresado {value} ES IMPAR')
else:
	print(f'El número ingresado {value} ES PAR')