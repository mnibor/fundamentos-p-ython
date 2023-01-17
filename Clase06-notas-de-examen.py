'''
Solicitar al operador que ingrese una calificación (entre 1 y 10)
Si la nota se encuentra entre 1 y 3 - Reprobó
Si la nota se encuentra entre 4 y 6 - Aprobó
Si la nota se encuentra entre 7 y 8 - Aprobó MUY BIEN
Si la nota se encuentra entre 9 y 10 - Aprobó SOBRESALIENTE
Considerar el ingreso incorrecto de un número.
'''

nota = int(input('Ingrese la nota asignada al exámen: '))
# resultado = ''

if (nota > 0) and (nota < 4):
    # Evalúo si la nota está entre 1 y 3
    resultado = 'Reprobó la materia'
elif (nota >= 4) and (nota <= 6):
    # Evalúo si la nota está entre 4 y 6
    resultado = 'Aprobó la materia'
elif (nota >= 7) and (nota <= 8):
    # Evalúo si la nota está entre 7 y 8
    resultado = 'Aprobó la materia MUY BIEN'
elif (nota >= 9) and (nota <= 10):
    # Evalúo si la nota está entre 9 y 10
    resultado = 'Aprobó la materia SOBRESALIENTE'
else:
    resultado = 'Ingresó un número incorrecto'

print(resultado)