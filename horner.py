#!/usr/bin/env python
# coding: utf-8

# In[31]:


def horner_desde_coeficientes(coeficientes, x):
    resultado=0;
    for i in range(0,len(coeficientes)):
        #Multiplicar al valor parcial el valor de x más el coeficiente
        resultado= resultado * x + coeficientes[i]
    return resultado


# In[40]:


def horner_desde_Polynomial( poly, x):
    coef = np.flip(poly.coef)
    return horner_desde_coeficientes( coef, x )


# In[44]:


from numpy.polynomial import Polynomial as Poly
import numpy as np

#desde coeficientes
coeficientes=[3, 4, 2, 3];
resultado = horner_desde_coeficientes(coeficientes, 2)        
print("Resultado:", resultado)

#desde numpy.polydomial
polinomio = Poly([3, 2, 4, 3])
resultado = horner_desde_Polynomial(polinomio, 2)        
print("Resultado:", resultado)

