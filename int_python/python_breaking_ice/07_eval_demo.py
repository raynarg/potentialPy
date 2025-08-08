"""
Evaluador de expresión
Pedí al usuario que ingrese una expresión matemática simple como texto ("5 + 3"), y evaluála con eval() para mostrar el resultado.
¡Explicá por qué eval() debe usarse con cuidado! 🔐

eval() deberia usarse con cuidado por el siguiente motivo:
el funcionamiento de eval() consiste en caso que tengamos que pasemos un input como parametro:
eval(input("ingrese un número"))
si ponemos 2 -> input -> "2" -> eval -> 2 (saca las comillas de string, que pone input)
"""

x = eval(input("ingrese una expresión matematica simple como texto: \n"))
print(x+3)