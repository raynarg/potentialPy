# Ex 2 Año Bisiesto - Por teclado
""" la logica de un try-except es que el codigo que pueda fallar
este dentro del try, dentro de except estara el codigo que se 
ejecuta en caso de fallar """
""" en la linea 9 tenia un if/else para devolver (true or false, bisiesto o no) pero
directamente es mejor poner un return en base a la expresion """

def bisiesto(n: int)->bool:
    return (n%4 == 0 and n%100 != 0) or (n%400 == 0)
try:
    anio = int(input("Ingrese un año: \n"))
    if anio > 0 and bisiesto(anio):
        print(anio, "es bisiesto")
    else:
        print(anio, "no es bisiesto")
except ValueError as e:
    print("error: ",e)