# VARIABLES

my_first_number = 75
my_second_number = 35

print('PRIMER VARIABLE:', my_first_number)
print('SEGUNDA VARIABLE:', my_second_number)

total = my_first_number + my_second_number
print('LA SUMA ES:', total)

# Buenas prácticas para definir variables

# 1º - Lo ideal sería utilizar variables en inglés
# 2º - No se pueden usar como nombre de variables, palabras reservadas del lenguaje  (Python)
# 3º - En Python, la identación del código SI IMPORTA
# 4º - No se pueden colocar números ni símbolos en el comienzo de los nombres de variable
# 5º - Se pueden usar acentos y la letra "ñ" pero se contradice con la regla #1
# 6º - Convenciones:
#                   formato kebab case: my-first-number, my-second-number
#                   formato camel case: myFirstNumber, mySecondNumber
#                   formato snake case: my_first_number, my_second_number
#                   formato train case: My_First_Number, My_Second_Number
# 7º - Constantes: se definen con el formato snake case y en mayúsculas todas las palabras. Su valor no debe ser modificado en tiempo de ejecución.
# 8º - NO EXPLICADO EN EL VIDEO. Debe tratarse, que el nombre de las variables, sean lo más descriptivas posible del dato que van a alojar. Por ejemplo si vamos a almacentar en una variable, el nombre de una fruta, lo más lógico es nombrar a esa variable como "fruit". Esto se hace para cuando tenemos que revisar un código, mucho tiempo después de que se escribió (suele suceder), entendamos a simple vista aún más el tipo de dato que maneja esa variable. Así también se aconseja evitar llamar a las variables con términos inteligibles, como X1, A1, X100. Las variables cuyos nombres están formados por una sola letra del alfabeto, se suelen usar para almacenar "contadores auxiliares" que no tienen peso en el código del programa. Este tema lo veremos mucho más adelante con más detenimiento.

MY_VALUE = 6.33

print(MY_VALUE)

myName = 'Marcelo'
liveIn = 'Buenos Aires'

print('Me llamo ' + myName + ' y vivo en ' + liveIn)

myName = 3
liveIn = 65

print('Me llamo ' + str(myName) + ' y vivo en ' + str(liveIn))

# Carácter informativo: posición de memoria
myName = 'Marcelo'
liveIn = 'Buenos Aires'

print(id(myName))
print(id(liveIn))

myName = 4
liveIn = 66

print(id(myName))
print(id(liveIn))

# Ejercicio propuesto: generar una variable para almacenar un nombre y un apellido. Otra variable para alojar el email y otra variable para alojar el número de teléfono. Mostrar por pantalla cada dato por separado y además quiero que lo muestren como un texto informativo: "Me llamo XXXX mi email es YYYY y mi número de teléfono es ZZZZ"

# Quiero anexar la edad en formato numérico y que se anexe al texto informativo: "Me llamo XXXX mi email es YYYY y mi número de teléfono es ZZZZ. Tengo CCCC años"

name = 'José Pérez'
email = 'joseperez@gmail.com'
telephone = '1122223333'
age = 38
ageTwo = '40'

print(int(telephone) + 10)

age = str(38)

print(name)
print(email)
print(telephone)
print(age)
print('')
print('Me llamo ' + name + ' mi email es ' + email + ' y mi número de teléfono es ' + telephone + '. Tengo ' + age + ' años.')



