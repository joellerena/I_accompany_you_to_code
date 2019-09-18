# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:16:45 2019
"""
base = int(input("Base: "))
expo = int(input("Exponente: "))
acum = 1
for i in range(expo):
    acum = acum * base
else:
    print(acum)