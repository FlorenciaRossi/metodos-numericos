import biseccion_un_paso
import sympy as sp
import math

# Definir la variable simbólica
x = sp.symbols('x')

# Definir la función 
#f = x**2 + 3*x + 2
#f = x**3 - 1
#f = x**3 -x +1
#f = sp.exp(-x) - sp.sin(x)
f = sp.abs(x - 5)
#Datos iniciales
a=0
b=7
xo = biseccion_un_paso.biseccion(f, a, b)
epsilon = 0.001 


def newton(f):
    error = 2 * epsilon
    xi = xo
    # Calcular la derivada
    der = sp.diff(f, x)
    
    if ( f.subs(x, xi) == 0):
        return xi
    
    while ( error >= epsilon):
        xn = xi - f.subs(x, xi) / der.subs(x, xi)
        error = abs( (xn -xi).evalf() )
        xi = xn
        print(xn.evalf())
        print(xi.evalf())
        print("error" ,error)
    return sp.N(xn , 4)             
    #sp.N(expr, <args>) : expresión sympy -> número decimal (aproximación)
    
    
print("Raíz aproximada de f(x)", newton(f))

#NO CONVERGE CON LAS SIGUIENTES FUNCIONES
#raix(x)
#2/x no tiene raíz

