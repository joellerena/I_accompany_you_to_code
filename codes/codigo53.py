# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:17:48 2019
"""
n = int(input("Ingrese un número: "))
while(n>1):
    if(n % 2 == 0):
        n = n // 2
    else:
        n = n * 3 + 1
    print(n, end=" ")
