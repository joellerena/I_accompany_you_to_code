# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:16:45 2019
"""
print("Base: ", end=" ")
base = int(input())
print("Exponente: ", end=" ")
expo = int(input())
acum = 1
for i in range(1, (expo+1), 1):
    acum = acum * base
else:
    print(acum)