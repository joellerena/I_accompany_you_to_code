# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:12:36 2019
"""
num1 = 3
num2 = 3.0
letra = "3"
num3 = 5
num4 = 3
conjunto = [1, 2, 3, 4]
palabra = "universidad"
lista1 = ["cristina","sebastián"]
tupla1 = ("cristina","sebastián")
#identidad
print("Identidad")
print("1: ",num1 is num2)
print("2: ",num1 is letra)
print("3: ",num1 is num3)
print("4: ",num1 is num4)
print("5: ",num1 is palabra)
print("6: ",lista1 is tupla1)
#pertenencia
print("Pertenencia")
print("7: ","univer" in palabra)
print("8: ",num1 in conjunto)