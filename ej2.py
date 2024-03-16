# -*- coding: utf-8 -*-
"""
2. Implementar en Python un proceso al estilo del anterior, pero que use dos funciones, una f y una g,
 y que la aplicación iterada sea una vez f, luego g, luego f, luego g, y así siguiendo, alternando una
 con otra, en total las veces que se especifique por el parámetro n, y finalmente devuelva el
 resultado obtenido tras la última aplicación.
"""

def aplica_f_g_n_veces(f,  g, x, n):
   resultado = x
   flagF = True
   for i in range(n):
        if ( flagF ):
            resultado = f(resultado)
            # print(resultado)
            flagF = False
        else:
            resultado = g(resultado)
            flagF = True
            # print(resultado)
   return resultado
  
def f(a):
    return a/2 - 1

def g(a):
    return (a*a) + 2

print("ultimo print", aplica_f_g_n_veces( f,g ,5,4))