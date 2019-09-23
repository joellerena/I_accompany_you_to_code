# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 06:01:28 2019
"""
def factorial(n):
    acum = 1
    for i in range(n):
        v = i+1
        acum = acum * v
    return acum
    
n = int(input("Ingrese n: "))
print("Factorial de ",n)
print("es ",factorial(n))
