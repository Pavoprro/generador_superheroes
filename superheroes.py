import random
def generar_nombre_aleatorio():
    base = random.choice(nombres_base)
    sufijo = random.choice(sufijos)
    return f"{base}{sufijo}"

def generar_nombre(base,sufijo):
    return f"{base}{sufijo}"

def asignar_habilidad(nombre, habilidad):
    return f"{nombre}tiene el superpoder de {habilidad}"

def asignar_equipo(nombre, equipo):
    return f"{nombre} pertenece al equipo {equipo}"

nombre_base=["el bicho","skibidi", "que", "si"]
sufijos=["siuuu","toile", "so", "no"]