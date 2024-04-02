# -*- coding: utf-8 -*-

a=int(input("ingrese valor a: "))
b=int(input("ingrese valor b: "))

#error tal que tenga los primeros 2 decimales correctos
epsilon =1/100
def biseccion(a, b):
    
    if not(sgn(p(b)) * sgn(p(a)) < 0):
        raise ValueError('No existe raíz en el intervalo dado')
        
    while b-a >= epsilon: #O OTRA CONDICIÓN
        
        #divido el intervalo a la mitad, ahí evaluaré la función 
        c=(a+b)/2
        
        #si f(c) -> c es raíz
        if p(c)==0:
            return c
        
        #si los sgn son distintos en ese intervalo [a, c] está la raíz
        #entonces en la prox iteración evaluo en [a , b (=c)]
        elif ( sgn(p(c)) * sgn(p(a)) < 0 ):
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
    
    
# FUNCIÓN

def p(x):
    return ( x*x*x ) - x + 1
    #return c - 2


resultado = biseccion(a,b)
print("Raíz aproximada: " , resultado)
