import random


def juego():
    jugador = input("Escoge entre'Piedra','Papel' o 'Tijera' meu filho \n").upper()
    jueguito = ["PIEDRA", "PAPEL", "TIJERA"]
    computadora = random.choice(jueguito)
    analisis = f"resultados: jugador coloco {jugador} e computadora coloco {computadora} es por eso que "

    if jugador == computadora:
        return f"{analisis} Empataste"
    
    if ganoJugador(jugador, computadora):
        return f"{analisis} Ganaste"

    return f"{analisis} dale de nuevo porque perdiste meu filho"
    

def ganoJugador(jugador, oponente):
    if ((jugador == "PIEDRA" and oponente == "TIJERA")
       or (jugador == "TIJERA" and oponente == "PAPEL")
       or (jugador == "PAPEL" and oponente == "PIEDRA")):
       return True
    else:
       return False

print(juego())