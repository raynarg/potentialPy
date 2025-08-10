"""
Tenés una lista de calificaciones de un curso, y querés:
Mostrar el número del estudiante (empezando en 1) junto con su calificación.
Marcar con (*) a aquellos que tengan una nota mayor o igual a 9.
Mostrar la cantidad total de estudiantes que cumplen la condición.

Datos:
calificaciones = [7.5, 9.0, 8.0, 10.0, 6.5, 9.5]
Salida esperada:
1 → 7.5
2 → 9.0 (*)
3 → 8.0
4 → 10.0 (*)
5 → 6.5
6 → 9.5 (*)
Total con nota destacada: 3"""

def alumnos_destacados(calificaciones: list[float]) -> str:
    lineas = []
    cant_alumnos_destacados = 0
    for i, v in enumerate (calificaciones, start=1):
        if v >= 9:
            lineas.append(f"{i} -> {v} (*)")
            cant_alumnos_destacados += 1
        else:
            lineas.append(f"{i} -> {v}")
    
    #podemos usar .join(lineas) porque es una lista de strings. Lo que hace join
    #es unir todos elementos de lineas es 1 solo string.
    resultado = "\n".join(lineas)
    resultado += f"\n Total alumnos con nota destacada {cant_alumnos_destacados}"
    return resultado

calificaciones = [7.5, 9.0, 8.0, 10.0, 6.5, 9.5]

print(alumnos_destacados(calificaciones))
