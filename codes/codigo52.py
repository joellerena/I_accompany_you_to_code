# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:56:20 2019
"""
x = int(input("Ingrese x: "))# x = 1
n = int(input("Ingrese n: "))# n = 3
acum = 0
for i in range(1, (n), 1):
    ii = i*2+1
    # potencia
    pot = 1
    for j in range(1, (ii+1), 1):
        pot = pot * x
    #factorial
    fac = 1
    for j in range(1, (ii+1), 1):
        fac = fac * j
    if(i % 2 == 1):
        acum = acum - (pot/fac)
    else:
        acum = acum + (pot/fac)
print("e^x = ", (acum+1))