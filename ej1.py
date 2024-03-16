# -*- coding: utf-8 -*-
"""
1. Implementar en Python el proceso anterior, que use una función (externa implementada,
o bien pasada como parámetro), que lea el x como parámetro y un n natural, y luego sobre 
el ex inicial aplique la f n veces, finalmente devolviendo el resultado obtenido tras la
 última aplicación.
"""

def funcion(x,  n):
   resultado = x
   for i in range(n):
        resultado = fun(resultado)
   return resultado
  
def fun(x):
    return x/2 - 1

print(funcion(2,3))
