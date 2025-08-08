# Ex 4 Ultimo digito de un número entero
"""
Para este ejercicio decidi focalizarme en algo simple, usando type casting para el (int -> str)
Al ser una cadena puedo facilmente identificar el ultimo digito usando como indice [-1].
"""

def last_digit (n: int) -> int:
    n_st = str(n)
    return int(n_st[-1])
n = int(input("ingrese numero entero: "))    
print(f"el último digito de {n} es: {last_digit(n)}")