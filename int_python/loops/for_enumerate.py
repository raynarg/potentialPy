"""
Queremos recorrer una lista de tareas y: Mostrar el número de tarea (empezando en 1). Mostrar el texto de la tarea.
Si la tarea contiene la palabra "URGENTE" (en mayúsculas), marcarla con un !.
Datos:
tareas = [
    "Comprar pan",
    "Enviar informe URGENTE",
    "Llamar al médico",
    "Pagar facturas URGENTE",
    "Hacer ejercicio"
]
Salida esperada:
1 → Comprar pan
2 → Enviar informe URGENTE (!)
3 → Llamar al médico
4 → Pagar facturas URGENTE (!)
5 → Hacer ejercicio


Vas a necesitar enumerate(..., start=1) para el número.
Usá un if "URGENTE" in tarea: dentro del loop para decidir si agregar el icono.
"""

def marcar_tarea_urgente(t: list) -> list: 
    if t is None:
        t = []
    for i, v in enumerate(t):
        if "URGENTE" in v:
            t[i] = v + " (!)"
    return t

def mostrar_lista_enumerada(t: list):
    for index, value in enumerate (t, start=1):
        print(f"{index} -> {value}")
        
tareas = [
    "Comprar pan",
    "Enviar informe URGENTE",
    "Llamar al médico",
    "Pagar facturas URGENTE",
    "Hacer ejercicio"
]

mostrar_lista_enumerada(marcar_tarea_urgente(tareas))







