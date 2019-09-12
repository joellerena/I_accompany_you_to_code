# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:27:20 2019
"""
num=int(input("Ingrese un número de tres cifras: "))
u=int(num % 10)
d=int(num % 100 /10)
c=int(num /100)
print("Unidad: ",u)
print("Decena: ",d)
print("Centena: ",c)
Arms = u*u*u + d*d*d + c*c*c
print("Número: ",num," = ",Arms)
print("Es Armstrong!!!")