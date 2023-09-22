import random
def mariposa():
    n = int(random.randint(0,50))
    matriz = [[0]*n for _ in range(n)]
    for j in range(n):
        matriz[0][j] = 1
        matriz[n -1][j]=1
    for i in range(1, n // 2 ):
        for j in range(i, n - i):
            matriz[i][j]= 1
            matriz[n- i-1][j] = 1
    for filas in matriz:
        for elementos in filas:
            print(elementos, end =" ")
        print()
    print(f"el tamaño de la matriz es: {n}")

    def matriz_ceros():
        #Imprime matriz cuadrada de tamaño n
        n=int(input("ingresa las dimensiones n: "))
        matriz=[[0]*n for _ in range(n)]
        for fila in range(n):#ciclo para llenar matriz
                for columna in range(n):     
                        matriz[fila][columna]= 1
        for fila in range(n):# Ciclo para imprimir
                for columna in range(n):
                        if (fila>=columna and columna<=5) or (fila<=columna and columna<=5):    
                #if columna==(n-fila-1):#cambio para inversa
                                print(0 , end=" ")
                        else:
                                print(matriz[fila][columna], end= " ")
                print()

