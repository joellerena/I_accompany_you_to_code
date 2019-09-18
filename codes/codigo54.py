# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:27:45 2019
"""
mayor = -999
for i in range(15, 21, 1):
    n = i
    cont = 0 
    print(n, end=": ")
    print(n, end=" ")
    while(n>1):
        if(n % 2 == 0):
            n = n // 2
        else:
            n = n * 3 + 1
        cont = cont + 1
        print(n, end=" ")
    if(cont >= mayor):
        mayor = cont
        num = i
    print()
print(num," genera la lista más larga con", mayor, "números")

