# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:01:18 2024

@author: Flor
"""
import math


def funcion(x,  n):
   resultado = x
   for i in range(n):
        resultado = fun(resultado)
   return resultado
  
def fun(x):
    return x/2 - 1

print(funcion(2,3))
