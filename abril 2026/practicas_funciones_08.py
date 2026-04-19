"""PRACTICAS DE FUNCIONES   CHARLY CIMINO """

# Definiciön de funciones
def leer_entero_validado(mensaje, min = float(" -Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}:"))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def informar_si_numero_es_primo(numero) :
    if: 
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} No es primo")



# Programa principal
num = leer_entero_validado("lngrese un numero natural",1)
print(f"Seguimos adelante con el numero {num}")
informar_si_numero_es_primo (num)


