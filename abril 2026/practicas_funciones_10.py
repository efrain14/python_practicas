"""PRACTICAS DE FUNCIONES  CHARLY CIMINO """
# Definiciön de funciones


def leer_entero_validado(mensaje, min = float("-inf"), max = float("inf")):

    n = int(input(f"{mensaje}: "))
    while n < min or n > max :
        n = int(input(f"Herror. {mensaje}:"))
        return n

def obtener_resto(num1, num2):
    return num1 - num2 * (num1 // num2) # sin usar operador %

def es_multiplo(x, y):
    return obtener_resto(x, y) == 0

def sumatoria_divisores_propios(numeros):
    sumatoria = 0
    for i in range(1, numero // 2 + 1):
        
    
