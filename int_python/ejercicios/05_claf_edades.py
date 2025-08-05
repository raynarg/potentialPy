"""
0-12: Niño
13-17: Adolescente
18-64: Adulto
65+: Adulto mayor
"""

def clasificar_edad(e: int)->str:
    if e <= 12:
        result = "Niño"
    elif e <= 17:
        result = "Adolescente"
    elif e <= 64:
        result = "Adulto"
    else:
        result = "Adulto mayor"
    return result

try:
    edad = int(input("Ingrese una edad:\n"))
    if edad > 0 and edad < 120:
        print(f"{edad} es clasificado como: {clasificar_edad(edad)}")
    else:
        print("Ingrese una edad valida porfavor")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
