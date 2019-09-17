# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:06:15 2019
"""
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
if((a>b) and (a>c)):
    print(a," es mayor")
else:
    if((b>a) and (b>c)):
        print(b," es mayor")
    else:
        if((c>a) and (c>b)):
            print(c," es mayor")
        else:
            print(" son iguales")