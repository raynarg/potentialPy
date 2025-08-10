"""
Últimos dos dígitos del DNI
Pedí al usuario su número de DNI y mostrá los últimos dos dígitos.
Asegurate de que el valor ingresado sea un número y tenga al menos dos dígitos."""

def pedir_dni()->int:
    while True:
        try:
            dni = int(input("Ingrese su DNI: "))
            if dni < 10:
                raise ValueError("DNI debe tener al menos 2 digitos")
            return dni
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un número de DNI válido.")

def ultimos_digitos(dni: int)->int: 
    return dni % 100

dni = pedir_dni()
print(f"Los últimos 2 digitos del DNI ingresado son: \n {ultimos_digitos(dni)}")
