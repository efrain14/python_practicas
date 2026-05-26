"""CADENA DE CARACTERES
Cada carácter en una cadena tiene una posición llamada índice. El índice es cero
basado, lo que significa que el índice del primer carácter de una cadena es 0, 
el índice del segundo carácter es 1, y así sucesivamente. Para acceder a un carácter
por su índice, utilizamos corchetes ( [] ) con el índice del carácter que deseas 
acceder dentro. Aquí hay algunos ejemplos:"""

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

"""La indexación negativa también está permitida, por lo que puedes obtener el 
último carácter de cualquier cadena con -1, el penúltimo carácter con -2, y así 
sucesivamente:"""

my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l