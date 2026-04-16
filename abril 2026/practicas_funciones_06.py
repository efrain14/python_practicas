""" EJERCICIO 06 FUNCIONES PYTHON EN 100 DIAS 
añade un color mediante un input al principio de la lista con el uso de una funcion"""

colores = ["rojo", "verde", "amarillo"]

def anadir_color(color) :
    """funcion que añade un color a al principio de la lista"""
    colores.insert(0, color)
    
anadir_color(input("escriba un color para añadirlo a la lista:\n"))
    
print(colores)