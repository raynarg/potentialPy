"""
Programa que recibe un caracter y determina si es un dígito, 
una letra mayúscula, una letra minúscula o un carácter especial.
Primero verifica si es dígito, si no, verifica si es letra; 
si no, entonces es un carácter especial.
Se utiliza la función isdigit() para verificar si es un dígito,
isalpha() para verificar si es una letra, y las funciones lower() y upper()
para determinar si es minúscula o mayúscula respectivamente.
"""

def caracter(l: str)->str:
    if l.isdigit():
        return "digito"
    else:
        if l.isalpha():
            if l == l.lower():
                return "minuscula"
            elif l == l.upper():
                return "mayuscula"
            else:
                return "unicode"
        else:
            return "caracter especial"

l = str(input("ingrese un caracter: \n"))

print(caracter(l))
