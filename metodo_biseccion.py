# -*- coding: utf-8 -*-

a=int(input("ingrese valor a"))
b=int(input("ingrese valor b"))
epsilon =1/100
def biseccion(a, b):
    while b-a>=epsilon:
        
        c=(a+b)/2
        print("paso ")
        print(c)
        
        if p(c)==0:
            return 0
        elif (sgn(p(c))*sgn(f(a))<0):
            b=c
        else:
            a=c
    
    return c

def sgn(z):
    if z==0:
        return 0
    elif z>0:
        return 1
    else:
        return -1
def f(c):
    return (c**5)+(c**4)+(2*(c**3))-100
def p(c):
    return (c**2) -2
resultado = biseccion(a,b)
