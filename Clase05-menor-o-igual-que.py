# Ejercicio: Ingresar dos valores y comprobar cual de los dos es menor O IGUAL que el otro

v1 = int(input('Ingrese V1 (un número entero): '))
v2 = int(input('Ingrese V2 (un número entero): '))

if v1 <= v2:
    print(f'Siendo V1 = {v1} y V2 = {v2}, se comprueba que V1 ES MENOR O IGUAL QUE V2')
else:
    print(f'Siendo V1 = {v1} y V2 = {v2}, se comprueba que V1 ES MAYOR QUE V2')