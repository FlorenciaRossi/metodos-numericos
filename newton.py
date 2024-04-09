import sympy as sp

from sympy import symbols, Abs
import math

#Datos iniciales
xo = 2
epsilon = 0.001 

# Definir la variable simbólica
x = sp.symbols('x')

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
        
    return sp.N(xn , 4)             
    #sp.N(expr, <args>) : expresión sympy -> número decimal (aproximación)
    
# Definir la función 
#f = x**2 + 3*x + 2
f = x**3 - 1
#f = x**3 -x +1
#f = sp.exp(-x) - sp.sin(x)
#f = Abs(x - 5)   

print("Raíz aproximada" , newton(f))

#NO CONVERGE CON LAS SIGUIENTES FUNCIONES
#raix(x)
