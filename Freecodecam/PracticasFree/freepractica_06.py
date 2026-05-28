"""FREECODECAM PRACTICAS
ASIGNACIONES AUMENTADAS"""

#Por ejemplo, aquí hay un ejemplo de uso de asignación aumentada para agregar 5 a una variable existente:
my_var = 10
my_var += 5

print(my_var) # 15

#Y aquí está lo mismo, pero sin asignación aumentada:

my_var = 10
my_var = my_var + 5

print(my_var) # 15

#El operador de asignación de resta (-=) resta el operando derecho de la variable izquierda y almacena la diferencia en la variable izquierda:

count = 14
count -= 3

print(count) # 11

#El operador de asignación de multiplicación (*=) multiplica la variable izquierda por el operando derecho y almacena el producto nuevamente en la variable izquierda:

product = 65
product *= 7

print(product) # 455

#El operador de asignación de división (/=) divide la variable izquierda por el derecho y almacena el resultado nuevamente en la variable izquierda:

price = 100
price /= 4

print(price) # 25.0

#El operador de división de piso (//=) realiza una división de piso de la variable izquierda por el derecho y almacena el resultado nuevamente en la variable izquierda:

total_pages = 23
total_pages //= 5

print(total_pages) # 4

#El operador de asignación módulo (%=) calcula el resto de la variable izquierda dividida por la derecha y lo almacena de nuevo en la variable izquierda:

bist = 35
bist %= 2

print(bist) # 1

#El operador de asignación de exponenciación (**=) eleva la variable izquierda a la potencia del derecho y almacena el resultado nuevamente en la variable izquierda:

power = 2
power **= 3

print(power) # 8

#También puedes usar algunos operadores de asignación aumentada con cadenas. Por ejemplo, el operador de asignación de suma facilita la concatenación de cadenas:

greet = "Hello"
greet += " Word"

print(greet) # Hello Word

#el operador de asignación de multiplicación puede usarse para repetir una cadena:

greet = "Hello"
greet *= 3

print(greet) # HelloHellohello



#Si te preguntas si los operadores de incremento y decremento (++  y -- ) funcionan
#en Python, no lo hacen. Eso es porque Python evita deliberadamente los atajos de
# incremento y decremento al estilo C para mantener el lenguaje claro y explícito.
#En lugar de x++, puedes simplemente escribir x += 1, lo cual deja claro que estás
# incrementando el valor de x en 1.
#Escribir ++x en Python solo aplica el signo más unario dos veces, y no incrementa
# nada:#

my_var = 5

print(+my_var)   # 5
#print(++my_var)  # 5
#print(+++my_var) # 5

my_var += 1

print(my_var) # 6