"""FUNCIONES DE AMBITO LOCAL las variables en una funcion siempre son de ambito local
las variables no se pueden llamar fuera de la funcion"""

def funcion():
    x = 10  # x es de ambito local
    print(x)
    
    
funcion()