# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:14:09 2019
"""
import math
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))
cociente1 = n1 / n2
cociente2 = int(n1 / n2) # parte entera sin redondeo
cociente3 = math.ceil(n1/n2)# redondeo hacia arriba
cociente4 = math.floor(n1/n2)# redondeo hacia abajo
cociente5 = round(n1 / n2)
print("Cociente1:    ", cociente1)
print("Cociente2 SR: ", cociente2)
print("Cociente3 CRArriba:", cociente3)
print("Cociente4 CRAbajo: ", cociente4)
print("Cociente5 CR: ", cociente5)
print("{:23.6f}".format(cociente1))
print("{:10.5f}".format(cociente1))# espacios blancos
print("{:010.5f}".format(cociente1))# con ceros
print("{:21d}".format(cociente2))# espacios blancos
print("{:4d}".format(cociente2))
print("{:3d}".format(cociente2))
print("{:2d}".format(cociente2))
print("{:1d}".format(cociente2))
print("{:04d}".format(cociente2))# con ceros
print("{:03d}".format(cociente2))
print("{:02d}".format(cociente2))
print("{:01d}".format(cociente2))