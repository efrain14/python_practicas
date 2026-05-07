"""ARGUMENTOS ARBITRARIOS   *ARGS Y **KWARGS  """

def funcion_combinada(*args, **kwargs):
    print("Argumentos de posicionales", args)
    print("Argumentos de palabra clave", kwargs)


funcion_combinada(1, 2, 3, nombre="juan", edad=25)