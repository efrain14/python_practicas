"""Build a Travel Weather Planner
Para este laboratorio, usarás sentencias condicionales para determinar si es posible desplazarte según el clima, la distancia a recorrer y la disponibilidad de un vehículo.

Objetivo: Cumplir con las historias de usuario a continuación y pasar todas las pruebas para completar el laboratorio.

User Stories:

1) Debes crear las siguientes variables:
distance_mi (un número que representa la distancia a recorrer en millas) valor = 5
is_raining (un booleano que representa si el usuario está experimentando clima lluvioso actualmente) valor = True
has_bike (un booleano que representa si el usuario tiene una bicicleta) valor = False
has_car (un booleano que representa si el usuario tiene un coche) valor = True
has_ride_share_app (un booleano que representa si el usuario tiene una app que le permite solicitar un viaje) valor = False
2) Debes usar sentencias condicionales para determinar si es posible el desplazamiento basado en los valores de estas variables.
3) Debes usar las sentencias if, elif y else para evaluar las categorías de distancia en orden ascendente.
4) Si distance_mi es un valor falso:
Deberías imprimir False.
5) Si la distancia es menor o igual a 1 milla:
Debes imprimir True solo si no está lloviendo.
De lo contrario, deberías imprimir False.
6) Si la distancia es mayor que 1 milla y menor o igual a 6 millas:
Debes imprimir True solo si la persona tiene una bicicleta y no está lloviendo.
De lo contrario, deberías imprimir False.
7) Si la distancia es mayor a 6 millas:
Debes imprimir True si la persona tiene un coche o tiene una aplicación de viaje compartido.
De lo contrario, deberías imprimir False."""

distance_mi = 5
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = False

if distance_mi == 0:
    print(False)
elif distance_mi <= 1 and not is_raining:
    print(True)
elif 1 < distance_mi <= 6 and not is_raining  and has_bike:
    print(True)
elif distance_mi < 6 and has_car and has_ride_share_app:
    print(True)
else:
    print(False)
    
print("\n"*3)

if distance_mi <= 0:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)