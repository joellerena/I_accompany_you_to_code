# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:40:44 2019
"""
n = int(input("Ingrese n: "))
a = -1
b = 1
for i in range(1, n+1):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
