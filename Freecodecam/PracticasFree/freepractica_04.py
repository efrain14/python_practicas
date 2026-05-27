"""PRACTICAS FREECODECAM  NUMEROS ENTEROS Y FLOTANTES
A veces, puedes notar que el resultado de una operación que involucra floats tiene 
más dígitos decimales de los esperados. Por ejemplo, la suma 0.1 + 0.2 es igual 
a 0.30000000000000004 en lugar de 0.3.
Esto sucede porque los números se almacenan en formato binario, y algunas fracciones
no pueden representarse exactamente en binario. Como resultado, se almacenan como 
aproximaciones finitas, de la misma manera que la fracción 1/3 no puede representarse
con un número finito de dígitos en decimal y se trunca después de cierto número de sus
dígitos infinitos (0.33333...).
Esto conduce a pequeños errores de redondeo.
Python también ofrece funciones incorporadas para convertir datos numéricos o cadenas 
de texto en enteros o flotantes.
La función float() devuelve un número de punto flotante construido a partir 
del número dado:"""

my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_int_1) # 56.0
print(type(my_float_1))  # <class "float">


#La función int() devuelve un entero construido a partir del número dado:

my_float = 12.92563
my_int = int(my_float)

print(my_int)  # 12
print(type(my_int))  # <class 'int'>


#También puedes usar las mismas funciones incorporadas para convertir una cadena de texto en un flotante o entero:

my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>