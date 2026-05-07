y = 20


def funcion():
    global y
    y = 30
    print(y, "imprecion dentro de la funcion")


funcion()
print(y, "imprecion fuera de la funcion")
