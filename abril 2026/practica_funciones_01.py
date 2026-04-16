""" EJERCICIO DE FUNCIONES PYTHON EN 100 DIAS 
"""

def saludar() :
    """funcion que da un saludo personalizado"""
    nombre = input("introdusca su nombre, por favor\n")
    print(f"muy buenas, {nombre.title()}")
saludar()