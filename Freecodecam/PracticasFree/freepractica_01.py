"""PRACTICAS FREECODECAM  NUMEROS ENTEROS E PUNTO FLOTANTE """
my_int_1 = 56
my_int_2 = -4

print(type(my_int_1))
print(type(my_int_2))


#Aqui esta como realizar una operacion de suma con enteros

my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print("SUMA DE ENTEROS", sum_ints)


#Aqui esta como realizar una resta de enteros

my_int_1 = 56
my_int_2 = 12

# Subtraction
diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints) # Integer Subtraction: 44

#Aqui esta como realizar una multiplicacion con enteros

my_int_1 = 12
my_int_2 = 4

# Multiplication
product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints) # Integer Multiplication: 48

#Y aquí es cómo realizar una operación de división con enteros

my_int_1 = 56
my_int_2 = 12

# Division
div_ints = my_int_1 / my_int_2
print('Division:', div_ints) # Division: 4.666666666666667

#Los flotantes son números positivos o negativos con puntos decimales, como 3.14, -0.5 o 0.0.
my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>


#Aquí está una operación de suma con flotantes:

my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition) # Float Addition: 17.4

#Aquí está una operación de resta con flotantes

my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction) # Float Subtraction: 6.6

#Aquí está una operación de multiplicación con flotantes:

my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication) # Float Multiplication: 64.80000000000001

#Y aquí es cómo realizar una operación de división con flotantes:

my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print('Float Division:', float_division) # Float Division: 2.222222222222222

#Si sumas un entero y un flotante, el resultado se convierte automáticamente en un flotante:

my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>