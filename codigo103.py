# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:40:22 2019
"""
import random as ra
acum = 0
print("Lanzamientos:")
for i in range(1,11):
    dado1 = ra.randint(1,6)
    dado2 = ra.randint(1,6)
    if(dado1 + dado2 == 7):
        acum = acum + 1
        print((i),"dado 1:",dado1,"dado 2:",dado2,
              "Suma 7, ¡GANASTE!")
    else:
        print((i),"dado 1:",dado1,"dado 2:",dado2)
print("Ganaste ",acum," veces ")
            
