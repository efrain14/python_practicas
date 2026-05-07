""" ARGUMENTOS POSICIONALES ARBITRARIOS CONOCIDOS COMO : *ARGS """

def suma_numeros(*numeros):
    print(numeros)
    resultado = sum(numeros)
    print(resultado)
    
    
suma_numeros(1, 2, 3, 4, 5, 6, 7)