import random


def adivina_el_numero_computadora(x):

    print("===================")
    print("Bienvenido al Juego")
    print("====================")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_superior

        respuesta = input(f"Mi prediccion es {prediccion}, si es muy alta ingresa (A), si es baja ingresa (B), si es correcta ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"A fucking dream!! la computadora adivino tu numero: {prediccion}")


adivina_el_numero_computadora(10)
