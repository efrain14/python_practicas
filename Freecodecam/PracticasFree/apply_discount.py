"""Construye una función Apply Discount
En este laboratorio escribirás una función que calcula el precio final de un artículo 
después de aplicar un descuento porcentual.
Debes definir una función llamada apply_discount.

La función apply_discount debe tomar exactamente dos parámetros: price y discount.

Si price no es un número (int o float), la función debe devolver la cadena The price should be a number.

Si discount no es un número (int o float), la función debe devolver la cadena The discount should be a number.

Si price es menor o igual a 0, la función debería devolver la cadena The price should be greater than 0.

Si discount es menor que 0 o mayor que 100, la función debe devolver la cadena The discount should be between 0 and 100.

Si ambas entradas son válidas, la función debe calcular el descuento como un porcentaje del precio.

La función debe devolver el precio final después de aplicar el descuento.

Tests:
:1. Debes tener una función llamada apply_discount.
:2. Tu función apply_discount debe tomar dos parámetros: price y discount.
:3. Cuando se llama a apply_discount con un price (primer argumento) que no es un número (int o float), debería devolver The price should be a number.
:4. Cuando se llama a apply_discount con un discount (segundo argumento) que no es un número (int o float), debe devolver The discount should be a number.
:5. Cuando se llama a apply_discount con un price menor o igual a 0, debería devolver The price should be greater than 0.
:6. Cuando se llama a apply_discount con un discount menor que 0 o mayor que 100, debe devolver The discount should be between 0 and 100.
:7. apply_discount(100, 20) debería devolver 80.
:8. apply_discount(200, 50) debería devolver 100.
:9. apply_discount(50, 0) debería devolver 50.
:10. Cuando se llama a apply_discount con un descuento de 100, debería devolver 0.
:11. apply_discount(74.5, 20.0) debería devolver 59.6."""

# paso 1) definir la estructura basica, Para empezar, declaramos nuestra función usando la palabra clave def, le asignamos el nombre requerido y definimos los dos parámetros de entrada: price (precio) y discount (descuento).
def apply_discount(price, discount):

# Paso 2) validar los tipos de datos (son numeros?),Antes de hacer matemáticas, debemos asegurarnos de que no nos hayan sumado "manzanas con letras". Usaremos la función nativa de Python isinstance() para verificar si las variables son de tipo entero (int) o flotante (float).
#Primero evaluamos el precio: Si no es un número, frenamos la ejecución inmediatamente con un return.     
    
    if not isinstance(price, (int, float)):
        return "The price shoul be a number."

#Luego evaluamos el descuento: Hacemos exactamente lo mismo para el segundo parámetro.

    if not isinstance(discount, (int, float)):
        return "The discount should be a number."
#Nota de clase: Usamos if separados porque si el precio falla, la función 
# termina ahí mismo y ni siquiera pierde tiempo revisando el descuento.

#Paso 3) Validar los rangos lógicos, Ahora que estamos seguros de que son números, 
# verificamos que tengan sentido en el mundo real.
#El precio debe ser mayor a 0: Si alguien intenta ingresar un precio de 0 o un 
# número negativo, devolvemos el error correspondiente.   

    if price <= 0:
        return "The price should be greater than 0."
    
#Paso 4) El descuento debe ser un porcentaje válido: Un porcentaje de descuento no puede
# ser menor a 0% ni mayor al 100%.
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100."
    
#Paso 5: Realizar la operación matemática y retornar
#Si el flujo de nuestro programa superó todas las "barreras" anteriores, significa
# que los datos son perfectos. Ahora procedemos al cálculo matemático.
#Para obtener el precio final, restamos al precio original el valor del descuento 
# aplicado. La fórmula matemática es: PRECIO FINAL = Precio - (Precio x Descuento)
#                                                                       ---------
#                                                                         100
#En Python, lo escribimos de una manera muy limpia y directa:
    final_price = price - (price * (discount / 100))
    return final_price

print(apply_discount(100, 20))     # Requerimiento 7  -> Devuelve: 80.0
print(apply_discount(200, 50))     # Requerimiento 8  -> Devuelve: 100.0
print(apply_discount(50, 0))       # Requerimiento 9  -> Devuelve: 50.0
print(apply_discount(120, 100))    # Requerimiento 10 -> Devuelve: 0.0
print(apply_discount(74.5, 20.0))  # Requerimiento 11 -> Devuelve: 59.6

# Pruebas de errores (Cosas que introducen mal los usuarios):
print(apply_discount("cien", 20))  # Devuelve: "The price should be a number."
print(apply_discount(100, [20]))   # Devuelve: "The discount should be a number."
print(apply_discount(-5, 20))      # Devuelve: "The price should be greater than 0."
print(apply_discount(100, 150))    # Devuelve: "The discount should be between 0 and 100."