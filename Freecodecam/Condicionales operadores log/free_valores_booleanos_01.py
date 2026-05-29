""" FREECODECAM BOOLEANOS  
Si estás trabajando con sentencias condicionales más complejas, puedes usar los operadores de Python and, or y not.

Pero antes de profundizar en esos operadores, veamos qué son los valores truthy y falsy.

En Python, cada valor tiene un valor booleano inherente, o un sentido incorporado de si debe ser tratado como True o False en un contexto lógico. Muchos valores se consideran truthy, es decir, evalúan a True en un contexto lógico. Otros son falsy, lo que significa que evalúan a False.
Aquí hay unos pocos valores falsos:

None
False
Entero 0
Flotante 0.0
Cadenas vacías ""
Otros valores como números distintos de cero y cadenas no vacías son verdaderos.

Si deseas verificar si un valor es truthy o falsy, puedes usar la función incorporada bool(). Esta convierte explícitamente un valor a su equivalente booleano y devuelve True para valores truthy y False para valores falsy. Aquí hay algunos ejemplos:"""

print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True

#Ahora que entiendes los valores truthy y falsy, podemos echar un vistazo a los operadores Booleanos, que también se conocen como operadores lógicos u operadores Booleanos. Estos son operadores especiales que te permiten combinar múltiples expresiones para crear una lógica de toma de decisiones más compleja en tu código.

#Hay tres operadores booleanos en Python: and, or y not.

#Primero echemos un vistazo al operador and.

#El operador and toma dos operandos y devuelve el primer operando si es falsy, de lo contrario, devuelve el segundo operando. Ambos operandos deben ser truthy para que una expresión resulte en un valor truthy.

#Aquí hay un ejemplo:

is_citizen = True
age = 25

print(is_citizen and age) # 25

#En el ejemplo anterior, el número 25 se imprime en la terminal porque el operador and evaluará el segundo operando si el primer operando es True. El operador and se conoce como un operador de cortocircuito. El cortocircuito significa que Python verifica los valores de izquierda a derecha y se detiene tan pronto como determina el resultado final.

#A menudo usarás and dentro de las sentencias if para verificar si se cumplen múltiples condiciones. Aquí te mostramos cómo puedes refactorizar el ejemplo anterior para usar el operador and en lugar de sentencias if anidadas:
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
    
#En el ejemplo anterior, is_citizen es True, y age >= 18 se evalúa como True. Dado que ambos operandos del operador and son verdaderos, la condición is_citizen and age >= 18 se evalúa como True, y se ejecuta la llamada a print dentro del bloque if.

#Ahora echemos un vistazo al operador or. Este operador devuelve el primer operando si es truthy, de lo contrario, devuelve el segundo operando. Una expresión con or resulta en un valor truthy si al menos un operando es truthy. El operador or también se conoce como un operador de cortocircuito. Aquí hay un ejemplo:  

age = 19
is_employed = False

print(age or is_employed) # 19

#El siguiente código imprimirá el número 19 porque el primer operando age es True.

#Si necesitas verificar si una o más expresiones son True, entonces puedes usar el operador or en una condición así:

age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')
    
#En este caso, age < 18 es False, pero is_student es True. Dado que al menos una condición es verdadera, toda la expresión or se evalúa como True, y se imprime el mensaje de descuento en el bloque if.

#El último operador que veremos es el operador not, que toma un solo operando e invierte su valor booleano. Convierte valores truthy en False y valores falsy en True. A diferencia de los operadores anteriores que vimos, not siempre devuelve True o False.

#Aquí hay algunos ejemplos: 
print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy

#Es común usar el operador not en condiciones para verificar si algo no es True o False, así:

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')

#Dado que is_admin es False, entonces not is_admin está diciendo no False, lo cual es True. Así que el mensaje Access denied for non-administrators. será impreso.

#Ahora que entiendes los valores truthy y falsy, los operadores and, or y not, y el funcionamiento del cortocircuito, puedes escribir lógica condicional más flexible y legible.

#CUAL ES LA SALIDA DEL SIGUIENTE CODIGO
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can watch the movie.")
else:
    print("You can't watch the movie.")