"""CADENA DE CARACTERES
El corte de cadenas te permite extraer una porción de una cadena o trabajar solo
con una parte específica de ella. Aquí está la sintaxis básica: string[start:stop]  
Si deseas extraer caracteres desde un cierto índice hasta otro, simplemente separa
los índices inicio y fin con dos puntos"""

my_str = 'Hello world'
print(my_str[1:4]) # ell

#Ten en cuenta que el índice finno es inclusivo, por lo que [1:4]solo extrae los 
# caracteres desde el índice 1, y hasta, pero sin incluir, el carácter en el índice 4.
#También puedes omitir los índices de inicioy fin, y Python tomará predeterminadamente
# 0 el final de la cadena, respectivamente. Por ejemplo, esto es lo que ocurre 
# si omite el índice de inicio:

my_str = 'Hello world'
print(my_str[:7])  # Hello w

#Esto extrae todo desde el índice 0 hasta (pero sin incluir), el carácter en el índice 7.
# Y esto es lo que ocurre si omite el índice de fin:

my_str = 'Hello world'
print(my_str[8:])  # rld

#Esto extrae todo desde el carácter en el índice 8 hasta el final de la cadena.
#Ten en cuenta que cortar una cadena no modifica la cadena original

my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)  # Hello world

#También puedes omitir tanto los índices de iniciocomo de fin, lo que extraerá 
# toda la cadena:

my_str = 'Hello world'
print(my_str[:])  # Hello world

#Además de los índices starty stop, también existe un parámetro opcional step, 
# que se usa para especificar el incremento entre cada índice en el segmento.
#Aquí está la sintaxis para eso:  string[start:stop:step]

#En el ejemplo a continuación, la división comienza en el índice 0, se detiene antes
# del 11, y extrae cada segundo carácter:

my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

#Un truco útil que puedes hacer con el parámetro paso es invertir una cadena configurando
# el paso a -1, y dejando en blanco inicioy fin

my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH