archivo = open(input("ingrese el nombre del archivo"), "r")

T = int(archivo.readline())

for i in range(T):
    Ni = int(archivo.readline())
    matriz = []
    for construirmatriz in range(Ni):
        fila = archivo.readline().split(" ")
        matriz.append(fila)

    trazamax = 0
    traza = 0
    for f in range(1, Ni):
        for h in range(Ni - f):
            for j in range(Ni - f):
                for k in range(f):
                    traza += int(matriz[k + h][k + j])
                    if trazamax < traza:
                        trazamax = traza

        print("La traza máxima posible para una submatriz de " + str(int(f)) + "x" + str(
            int(f)) + "de la matriz número" + str(int(i + 1)) + "es:", trazamax)

archivo.close()