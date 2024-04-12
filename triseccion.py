#a=int(input("ingrese valor a: "))
#b=int(input("ingrese valor b: "))
a = -2
b = 3

#error tal que tenga los primeros 2 decimales correctos
epsilon =1/100
def triseccion(a, b):
    
    if not(sgn(p(b)) * sgn(p(a)) < 0):
        raise ValueError('No existe raíz en el intervalo dado')
        
    while b-a >= epsilon: #O OTRA CONDICIÓN
        
        #divido el intervalo en tres, ahí evaluaré la función 
        c = (2 * a + b) / 3
        d = (a + 2 * b) / 3     
        
        #si f(c) -> c es raíz
        if p(c) == 0:
            return c
        if p(d) == 0:
            return d
        
        #si los sgn son distintos en ese intervalo [a, c] está la raíz
        #entonces en la prox iteración evaluo en [a , b (=c)]
        elif ( sgn(p(c)) * sgn(p(a)) < 0 ):
            b=c
        #si los sgn son distintos en ese intervalo [c, d] está la raíz
        #entonces en la prox iteración evaluo en [a(=c) , b (=d)]
        elif (sgn(p(c)) * sgn(p(d)) < 0):
            a = c
            b = d
        #si no, en el intervalo [a, d] no hay raíz
        #prox iteración evaluo en [ a (=d), b]
        else:
            a=d
    
    return (a + b) / 2


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
    return ( x*x*x ) - 1
    #return c - 2


resultado = format(triseccion(a,b) , '.2f')
print("Raíz aproximada: " , resultado)