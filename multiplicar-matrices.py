#[[col0], [col1], [col2]]
matrizA = [[1, 4],[2, 5],[3, 6]]
matrizB = [[5, 1, -2],[-1, 0 , 3]]
mC = [[1,1,0], [2,1,1], [3,1,-1]]
def getMatriz(m):
    # i -> columna
    # j -> fila
    for i in range(len(m[0])):
        for j in range(len(m)):
            print(m[j][i], end = " ")
            
        print()

def numColumnas(m):
    return len(m)

def numFilas(m):
    return len(m[0])

#m[col][fila]
def multiplicar(m, n):
    if ( numColumnas(m) != numFilas(n)):
        raise ValueError("No se pueden multiplicar las matrices")
    mNueva = [[0] * numFilas(m) for _ in range(numColumnas(n))]
    #mNueva = [ [0] * numFilas(m) ] * numColumnas(n)
    #lleno por filas
    for i in range(len(m[0])):   
        #k columna de n
        for k in range(len(n)):
            elementoij = 0
            for j in range(len(n[0])):
                elementoij = elementoij + m[j][i] * n[k][j]
            mNueva[k][i] = elementoij
    return mNueva

print("matrizA:")      
getMatriz(matrizA)
print("matrizB: ")
getMatriz(matrizB)
m= multiplicar(matrizA,matrizB)
print("matrizA x matrizB: ")
getMatriz(m)
print("mC x mC")
getMatriz(multiplicar(mC, mC))
