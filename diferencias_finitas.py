def lista_siguiente(numeros):
    lista2 = []
    for i in range(len(numeros)-1):
        lista2.append(numeros[i+1] - numeros[i])
    return lista2

def elementos_son_iguales(lista):
    anterior = lista[0]
    flag = True
    for e in lista:
        if anterior != e:
            flag = False
    return flag

def ultimos_elementos(numeros, lista):
    lista.append(numeros[-1])
    if len(numeros) > 1 and not elementos_son_iguales(numeros):
        ultimos_elementos(lista_siguiente(numeros), lista) 
        
def diferencias_finitas(numeros):
    miLista = []
    ultimos_elementos(numeros, miLista)
    resultado = 0
    for i in range(len(miLista)):
        resultado = resultado + miLista[-1-i]
    return resultado

#numeros = [3, 2, 8, 5]
numeros = [1, 3, 5, 7, 9]
print(diferencias_finitas(numeros))