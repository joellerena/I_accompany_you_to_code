# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 07:28:01 2019
"""
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
if(a>b):
    if(a>c):
        print(a," es mayor")
    else:
        print(c," es mayor")
else:
    if(b>c):
        print(b," es mayor")
    else:
        print(c," es mayor")