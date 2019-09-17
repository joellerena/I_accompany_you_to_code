# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:11:58 2019
"""
def fibonacci(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    return(fibonacci(n-1)+fibonacci(n-2))

n = int(input("Ingrese n: "))
for i in range(0, n):
    print(fibonacci(i), end=" ")