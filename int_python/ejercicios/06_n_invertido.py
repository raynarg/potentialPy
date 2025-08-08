"""
Número invertido (3 cifras)
Pedí un número de 3 cifras y mostrálo al revés.
---
Para cumplir con la consigna opte por hacer 2 soluciones completamente distintas:
    Opción[1]: Utilizar la estructura de control de flujo for en conjunto con la
    función built-in range(). (Queria complicarme y acordarme de como se usaba range())
    Opción[2]: Utilizar una operación particular sobre Strings -> String Slicing
    manera más "pythonica"
"""
""" #Opción1
def int_inverter_range(n: int)->int: 
    n_str = str(n)
    inv_str = ""

    for value in range(len(n_str) - 1, -1, -1):
        inv_str += n_str[value]
    
    result = int(inv_str)
    return result """

""" number = int(input("\nIngrese un número entero porfavor: "))
print(f"\nEl número invertido es: {int_inverter_range(number)}") """

#Opción2
def int_inverter_slice(n: int)->int: 
    n_str = str(n)
    inv_str = n_str[::-1]
    result = int(inv_str)
    return result

number = int(input("\nIngrese un número entero porfavor: "))
print(f"\nEl número invertido es: {int_inverter_slice(number)}")