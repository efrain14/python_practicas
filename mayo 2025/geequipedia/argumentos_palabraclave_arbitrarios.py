""" ARGUMENTOS DE PALABRA CLAVE ARBITRARIOS CONOCIDOS COMO **KWARGS """

def imprimir_info(**info):
    print(info)
    for clave, valor in info.items():
        print(f"{clave}: {valor} ")




imprimir_info(nombre="juan", edad=25, ciudad="caracas")