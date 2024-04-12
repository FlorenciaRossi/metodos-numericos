""" Metódo de trisección para aproximar raíces """

#DATOS INICIALES
a=int(input("Ingrese valor a: "))
b=int(input("Ingrese valor b: "))
epsilon =1/100

def method_triseccion(p, a, b):
    
    if not(sgn(p(b)) * sgn(p(a)) < 0):
        raise ValueError('No existe raíz en el intervalo dado')
        
    while b-a >= epsilon:
        
        #divide el intervalo en tres
        c = (2 * a + b) / 3
        d = (a + 2 * b) / 3     
        
        if p(c) == 0:
            return c
        if p(d) == 0:
            return d
        
        #evalua en qué intervalo se encuentra la raíz
        elif ( sgn(p(c)) * sgn(p(a)) < 0 ):
            b=c
        elif (sgn(p(c)) * sgn(p(d)) < 0):
            a = c
            b = d
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
def f(x):
    return ( x*x*x ) - 1
    #return c - 2


resultado = format(method_triseccion(f, a, b) , '.2f')
print("Raíz aproximada de la función en el intervalo [", a, ", ",b,"]:" , resultado)
