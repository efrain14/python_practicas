"""CADENA DE CARACTERES
Cuando trabajas con cadenas, combinar diferentes fragmentos de texto es una operación común con la que a menudo te encontrarás.

En Python, puedes combinar múltiples cadenas juntas con el operador más ( +). 
Este proceso se llama concatenación de cadenas . Aquí te mostramos cómo concatenar
dos cadenas con el operador más:"""

my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

# Pero ten en cuenta que esto solo funciona con cadenas. Si intentas concatenar
# una cadena con un número, obtendrás un TypeError:
#name = 'John Doe'
#age = 26

#name_and_age = name + age
#print(name_and_age) # TypeError: can only concatenate str (not "int") to str

#Esto sucede porque Python no convierte automáticamente otros tipos de datos como
# enteros en cadenas cuando los concatenas. Python requiere que todos los elementos
# sean cadenas antes de poder concatenarlos. Para solucionarlo, puede convertir 
# el número en una cadena con la función incorporada str(), que devuelve la 
# representación de cadena del objeto dado sin modificar el objeto original:

name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26

#También puedes usar el operador de asignación aumentada para la concatenación.
# Este se representa con un más y un signo igual ( +=), y realiza tanto la concatenación
# como la asignación en un solo paso. Aquí tienes cómo funciona:

name = 'Efrain Garcia'
age = 58

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26