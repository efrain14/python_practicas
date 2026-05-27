"""PRACTICAS FREECODECAM  NUMEROS ENTEROS Y FLOTANTES
Aquí hay algunos otros métodos que Python ofrece para trabajar con enteros y flotantes."""

#round(): Redondea un número a un número especificado de lugares decimales. Por defecto, esta función redondea al entero más cercano y devuelve un número entero sin lugares decimales:

my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

#abs(): devuelve el valor absoluto de un número,

num = -15

absolute_value = abs(num)
print(absolute_value) # 15

#pow(): eleva un número a la potencia de otro o realiza exponentiación modular.

result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3