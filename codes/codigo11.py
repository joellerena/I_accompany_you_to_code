# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:22:57 2019
"""
t = "palabra," #string
n = 23 #entero
print("Una palabra,",t,"ahora un número",n)
m = "Una palabra, {} ahora un número '{}'".format(t,n)
print(m) #uso de función de formato a referencia
print(3 * t + t) #triplicar string y concatenar