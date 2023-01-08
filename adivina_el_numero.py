import random


def adivina_el_numero(x):

    print("Seja bem vindo á brincadeira")
    print("-----------------------")
    print("Your goal is to guess the number")

    numero_aleatorio = random.randint(1, x)

    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Advina entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("intenta otra vez")
        elif prediccion > numero_aleatorio:
            print("es mucho, wey")

    print(f"felicitaciones ya ganaste {numero_aleatorio} era correcto")


adivina_el_numero(10)