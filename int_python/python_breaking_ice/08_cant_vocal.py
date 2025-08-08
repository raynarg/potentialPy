"""
Opte por usar un Set como estructura de datos, debido a que en este caso los elementos no se repiten
ni tampoco mantienen un orden. Y ademas es mas eficiente para usar con el operador in.
"""
def cantidad_vocales(t: str) -> int:  
    texto = t.lower()
    vocales_set = {"a","e","i","o","u"}
    cont = 0
    for letra in texto:
        if letra in vocales_set:
            cont += 1    
    return cont

texto = input("ingrese un texto: \n")
print(cantidad_vocales(texto))



    

