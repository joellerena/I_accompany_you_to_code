# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:59:08 2019
"""
import random as ra
adivina = ra.randint(1,100)
contar = 0
n = -99
while(n != adivina):
    n = int(input("Ingrese un número:"))
    if((n!=adivina)):
        if(n > adivina):
            print("Ingrese un número más bajo")
        else:
            print("Ingrese un número más alto")
    contar = contar + 1
print("GANASTE!! en el intento", contar)
