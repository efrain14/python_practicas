"""CADENA DEE CARACTERES
Las cadenas son tipos de datos inmutables en Python. Esto significa que puedes
reasignar una cadena diferente a una variable:"""

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

#Pero no se permite la modificación directa de una cadena:

greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment