import numpy as np
import random
import time

def generar_matrices():
    file = open('input.txt', mode= "w")
    casos = random.randrange(100)
    print( str(casos) + ' \n' )
    file.write( str(casos) + '\n' )
    for _ in range(casos):
        tam = random.randrange(100)
        file.write( str(tam) + '\n' )
        matriz = np.floor(np.random.rand(tam,tam) * 100).astype(int)
        for i in range(tam):
            for j, x in  enumerate(matriz[i]):
                file.write( str(x) )
                if j != tam - 1:
                    file.write( " " )
            file.write("\n")
    file.close()


#generar_matrices()


def calcular_traza_maxima(matriz):
    traza_maxima = np.matrix.trace(matriz)
    for i in range(matriz.shape[0]):
        tr1 = np.matrix.trace(matriz, offset= i)
        tr2 = np.matrix.trace(matriz, offset= -i)
        traza_maxima = max(traza_maxima, tr1, tr2)
    return traza_maxima


def main():
    entrada = open('input.txt', mode= 'r')
    salida = open('salida.txt', mode= 'w')

    for  j in range(1, int(entrada.readline()) + 1):
        tam = int(entrada.readline())
        matriz = np.zeros( shape = (tam, tam ))
        for i in range(tam):
            fila = entrada.readline().split(" ")
            fila = [ int(x) for x in fila]
            matriz[i] = fila
        resultado =  str( calcular_traza_maxima(matriz))
        salida.write("Matriz " +  str(j) + ": " + resultado + "\n"  )

    entrada.close()
    salida.close()


inicio = time.time()
main()
fin = time.time()
print("Tiempo: ", fin - inicio)


