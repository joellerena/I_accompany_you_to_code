# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 06:01:28 2019
"""
def fibonacci(n):
    a = -1
    b = 1
    for i in range(n):
        c = a + b
        print(c,end=" ")
        a = b
        b = c
   
n = int(input("Ingrese enésimo término: "))
print("Serie de Fibonacci de ",n, end=" ")
print("es: ")
fibonacci(n)