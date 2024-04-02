import math

a=int(input("ingrese valor a: "))
b=int(input("ingrese valor b: "))

maxPasos = 3
# epsilon =1/1000

def biseccion(a, b):
    pasos = 0
    if not(sgn(f(b)) * sgn(f(a)) < 0):
        raise ValueError('No existe raíz en el intervalo dado')
        
    while pasos <= maxPasos: #O OTRA CONDICIÓN
        pasos += 1
        #divido el intervalo a la mitad, ahí evaluaré la función 
        c=(a+b)/2
        
        #si f(c) -> c es raíz
        if f(c)==0:
            return c
        
        #si los sgn son distintos en ese intervalo [a, c] está la raíz
        #entonces en la prox iteración evaluo en [a , b (=c)]
        elif ( sgn(f(c)) * sgn(f(a)) < 0 ):
            b=c
        #si no, en el intervalo [a, c] no hay raíz
        #prox iteración evaluo en [ a (=c), b]
        else:
            a=c
    
    return c


#FUNCIÓN SIGNO
def sgn(z):
    if z==0:
        return 0
    elif z>0:
        return 1
    else:
        return -1
    
    
# FUNCIONES
def f(x):
    #return  ( 2 * x )  + 3
    #return ( math.e ** (-x) ) - math.sin(x)
    return ( x*x*x ) - x + 1
    #return ( x*x*x ) + 1
    




resultado = biseccion(a,b)
print("Raíz aproximada: " , resultado)
