# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:22:01 2019
"""
def factorial(n):
    if (n>0):
        return (n * factorial(n-1))
    else:
        return 1

n = int(input("Ingrese n: "))
for i in range(1, n+1):
    print(factorial(i), end=" ")
