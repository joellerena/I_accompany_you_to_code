# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:53:47 2019
"""
cantidad = int(input("Ingrese la cantidad del producto: "))
precio = 1
subtotal = cantidad * precio
IVA = subtotal * 0.12
total = subtotal +  IVA
print("Subtotal: ",subtotal)
print("IVA: ",IVA)
print("total: ",total)