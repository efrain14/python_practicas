""" EJERCICIO DE FUNCIONES 05 PYTHON EN 100 DIAS 
FUNCION CALCULADORA DE SUMA USANDO RETURN """

def suma(numero1, numero2):
    """funcion que suma 2 numeros y muestra el resultado"""
    print(numero1 + numero2)
suma(10, 50)

def suma1(numero1, numero2):
    """funcion que suma 2 numeros y almacena la informacion de el resultado para usarla en el programa"""
    return numero1 + numero2

resultado = suma1(10, 50)

print(resultado)
