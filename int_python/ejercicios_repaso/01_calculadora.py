# Ex 1 Calculadora
"""
-Calculadora simple que permite realizar operaciones básicas: suma, resta, multiplicación y división.
-Busque anticipar en el caso de la funcion div, que el segundo operando sea distinto de 0 
para evitar una op. indefinida.
-Algo que no me acordaba era castear o pasar la input del usuario al tipo de variable que yo necesito (float)
"""

def suma(n1: float, n2: float) -> float:
    return n1 + n2
def resta(n1: float, n2: float) -> float:
    return (n1) - (n2)
def mult(n1: float, n2: float) -> float:
    return n1 * n2
def div(n1: float, n2: float) -> float:
    if n2 == 0:
        raise ValueError("No se puede dividir por cero")
    return n1 / n2
aux = True
opt = 0
result = 0

# Loop para que el usuario pueda realizar varias operaciones, decidi que el tipo de dato de aux sea bool
while aux == True:
    n1 = float(input("inserte primer numero: "))
    n2 = float(input("inserte segundo numero: "))

    # Para hacer mas robusta la operación, se puede agregar un try-except
    while True:
        try:
            opt = int(input("Elija operación: \n1)Suma, 2)Resta, 3)Multiplicacion, 4)División \n"))
            if 1 <= opt <= 4:
                break
            else:
                print("Ingrese una opción entre 1 y 4")
        except ValueError:
            print("Ingrese una opción valida")

    if opt == 1:
        result = suma(n1, n2)
    elif opt == 2:
        result = resta(n1, n2)
    elif opt == 3:
        result = mult(n1, n2)
    elif opt == 4:
        try:
            result = div(n1, n2)
        except ValueError as e:
            print(f"Error: {e}")
            continue
    else:
        print("Operación no válida")

    print(f"El resultado es: {result}")
    check = input("¿Desea continuar? (s/n): ").lower()
    aux = check == 's' 