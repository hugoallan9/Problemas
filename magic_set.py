


def determinar_sucesiones_buenas(lista, m):
    #Verificando si los numeros son multiplos de m
    contador = 0
    for x in lista:
        if x % m == 0:
            contador = contador + 1

    if contador == 0:
        return 0
    else:
        return 2**contador - 1


T = int( input() )

for i in range(T):
    lista_temp = []
    tam_lista, m  =  input().split(" ")
    tam_lista, m = int(tam_lista), int(m)
    lista_temp = [int(x) for x in input().split(" ")]
    print( determinar_sucesiones_buenas(lista_temp, m) )




