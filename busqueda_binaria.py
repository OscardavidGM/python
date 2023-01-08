import random
import time


def busquedaIngenua (objetivo, lista):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busquedaBinaria (objetivo, lista, limiteInferior=None, limiteSuperior=None):
    if limiteInferior is None:
        limiteInferior = 0
    if limiteSuperior is None:
        limiteSuperior = len(lista)-1

    if limiteSuperior > limiteInferior:
        return -1
    
    puntoMedio = (limiteInferior + limiteSuperior) // 2 

    if lista[puntoMedio] == objetivo:
        return puntoMedio
    elif objetivo < lista[puntoMedio]:
        return busquedaBinaria(objetivo, lista, limiteInferior, puntoMedio-1)
    else: 
        return busquedaBinaria(objetivo, lista, puntoMedio+1, limiteSuperior)

if __name__=='__main__': # Esta parte del codigo solo funciona en el archivo original y no importandolo

    tamaño = 10000
    setInicial = set()

    while len(setInicial) < tamaño:
        setInicial.add(random.randint(0, 10000))

    listaOrdenada = sorted(list(setInicial))

# BusquedaIngenua

    inicio = time.time()

    for objetivo in listaOrdenada:
        busquedaIngenua(objetivo, listaOrdenada)
    
    fin = time.time()
    print(f"Tiempo de busqueda de BusquedaIngenua {fin - inicio}")

# BusquedaBinaria

    inicio = time.time()

    for objetivo in listaOrdenada:
        busquedaBinaria(objetivo, listaOrdenada)

    fin = time.time()
    print(f"Tiempo de busqueda de BusquedaBinaria {fin - inicio}")