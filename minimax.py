import numpy as np


def obtenerMinimos(m):
    resultados = np.array(len(m))
    for i in range(len(m)):
        resultados[i] =  min(m[i])
    return resultados

def obtenerMaximos(m):
    resultados = np.array( len(m))
    for j in range(len(m)):
        resultados[j] =  max(m[:,j])
    return resultados

def obtenerNumeroCambios(m):
    maximos_minimos = max(obtenerMinimos(m))
    minimos_maximos = min( obtenerMaximos(m) )
    if maximos_minimos == minimos_maximos:
        return 0
    else:
        #Obteniendo cuantos elementos por fila son mas pequeños que el maxmin
        #Y cuantos elementos por columna son mas grandes que el minmax 
        for



N = input("")

matriz = []

for _ in range(N):
    fila = []
    fila = [x for x in input().split(" ")]
    matriz.append(fila)

