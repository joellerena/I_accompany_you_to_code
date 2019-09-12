# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:21:21 2019
"""
num=int(input("Ingrese un número de cuatro cifras: "))
u=int(num % 10)
d=int(num % 100 /10)
c=int(num /100) % 10
m=int(num / 1000)
print("Unidad: ",u)
print("Decena: ",d)
print("Centena: ",c)
print("Miles: ",m)
Arms = u*u*u*u + d*d*d*d + c*c*c*c + m*m*m*m
print("Número: ",num," = ",Arms)
print("Es Armstrong!!!")
