import math
import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

maxPasos = 1


def biseccion(f, a, b):
    pasos = 0
    if not(sgn(f.subs(x, b)) * sgn(f.subs(x, a)) < 0):
        raise ValueError('No existe raíz en el intervalo dado')
        
    while pasos <= maxPasos: #U OTRA CONDICIÓN
        pasos += 1
        #divido el intervalo a la mitad, ahí evaluaré la función 
        c=(a+b)/2
        
        #si f(c) -> c es raíz
        if f.subs(x, c) ==0:
            return c
        
        #si los sgn son distintos en ese intervalo [a, c] está la raíz
        #entonces en la prox iteración evaluo en [a , b (=c)]
        elif ( sgn(f.subs(x, c)) * sgn(f.subs(x, a)) < 0 ):
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
    


