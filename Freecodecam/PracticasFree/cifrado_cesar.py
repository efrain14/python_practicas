""""crearás un programa llamado cifrado César, que es un método de encriptación que desplaza letras en el alfabeto para codificar mensajes.

Comienza creando una variable llamada shift y asigna el valor 5 a tu nueva variable.
Declara otra variable llamada alphabet y asigna la cadena abcdefghijklmnopqrstuvwxyz a esta variable.
vas a construir un cifrado de César. Ésta es una de las técnicas más simples para encriptar texto, que consiste en sustituir cada letra del texto plano con la letra que se encuentra a un número fijo de posiciones hacia abajo en el alfabeto. Por ejemplo, con un desplazamiento de 5, a se reemplazaría por f, b por g y así sucesivamente.

Para implementar este cifrado, necesitarás crear una nueva versión de tu alfabeto que comience en la posición indicada por el desplazamiento. Como aprendiste en una lección anterior, puedes extraer parte de una cadena usando el corte de cadenas (string slicing):
Crea una variable llamada shifted_alphabet y usa la sintaxis de segmentación para asignarle la porción de alphabet que comienza en el índice de shift. Luego, llama a la función incorporada print() para imprimir shifted_alphabet en la terminal y observa el resultado."""


shift = 5
alphabet = "abcdefghijklmnopqrstuvwxyz"
shifted_alphabet = 