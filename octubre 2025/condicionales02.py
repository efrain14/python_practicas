""" Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable 
sin tener en cuenta mayúsculas y minúsculas."""

CONTRASENA = "mundomagico123"
contrasena = str(input("escriba la contraseña: ").lower())
if CONTRASENA == contrasena:
    print("la contraseña es correcta")
else:
    print("la contrasea es incorrecta, intente de nuevo")




