"""PARAMETROS POR DEFECTO EN LAS FUNCIONES CON PYTHON  CHARLY CIMINO """

#dEFINICION DE FUNCIONES
def presentar(nombre = "anonimo", edad = 50) :
    print(f"Hola soy {nombre}, y tengo {edad} años de edad")
presentar("juan", 27)
presentar("maria")
presentar()