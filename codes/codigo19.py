# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:05:19 2019
"""
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))
cociente1 = n1 / n2
cociente2 = int(n1 / n2) # parte entera sin redondeo
residuos = (n1 % n2)
print("Cociente: ", cociente1)
print("Cociente: ", cociente2)
print("Residuo: ",residuos)