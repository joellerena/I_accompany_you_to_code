# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:55:57 2019
"""
n = int(input("Ingrese un número: "))
acum = 1
for i in range(0,n):
    print((i+1),end=" ")
    acum = acum * (i+1)
print(" = ",acum)
