import random
import string

from palabras import palabras
from ahorcadoimagen import vidas_diccionario_visual

def obtener_palabra(lista_palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
        
    return palabra.upper()

def ahorcado():
      
      print ("Bienvenido al juego del ahorcado")

      palabra = obtener_palabra(palabras)

      letras_por_adivinar = set(palabra)
      letras_adivinadas = set()
      abecedario = set(string.ascii_uppercase)

      vidas = 7

      while len(letras_por_adivinar) > 0 and vidas > 0:
        if vidas > 1:
          print(f"te quedan {vidas} vidas y has usado estas letras: {' '.join (letras_adivinadas)}")
        else:
          print(f"te queda {vidas} vida y has usado estas letras: {' '.join (letras_adivinadas)}")

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"palabra {' '.join(palabra_lista)}")

        letra_usuario = input("escoge una letra:  ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(' ')
            
            else:
                vidas -= 1
                print (f"\nTu letra {letra_usuario} no está")
        elif letra_usuario in letras_adivinadas:
            print ("\nYa escogiste esta letra, coloca otra")
        else:
            print ("Esa letra no es valida")
      if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado, la palabra era \n{palabra}")
      else:
        print(f"adivinaste, eres un ganador meu filhoo, adivinaste la palabra {palabra}")

ahorcado()