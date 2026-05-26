"""CADENA DE CARACTERES
El proceso de insertar variables y expresiones en una cadena se llama interpolación
de cadenas . Python tiene una categoría de cadena llamada f-strings 
(abreviatura de literales de cadena formateados), que te permite manejar la interpolación
con una sintaxis compacta y legible.
Las cadenas f comienzan con f(ya sea en minúsculas o mayúsculas) antes de las comillas
y te permiten insertar variables o expresiones dentro de campos de reemplazo indicados
por llaves ( {} ). Aquí tienes un ejemplo:"""

name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

#Observa que no necesitas convertir tipos no cadena con la función str(). En el
# ejemplo anterior, el valor de las variables age, num1y num2se convierte internamente
# en una cadena durante el proceso de interpolación.