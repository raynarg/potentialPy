"""
Ejercicio: Clasificar días de la semana con match case
Pedí al usuario que ingrese el nombre de un día de la semana (por ejemplo: “lunes”, “martes”, etc.).
Usá match case para imprimir si el día es:
“día laboral” (lunes a viernes)
“fin de semana” (sábado o domingo)
“día inválido” si no corresponde a un día válido

Pista: Conviene usar .lower() para que no importe si el usuario pone mayúsculas o minúsculas."""

def day(d:str)->str: #type:ignore
    d = d.lower()
    match d:
        case "lunes"|"martes"|"miercoles"|"jueves"|"viernes":
            return "dia laboral"
        case "sabado"|"domingo":
            return "fin de semana"
        case _:
            return "dia inválido"
d = input("ingrese un dia porfavor: ")
print(day(d))        