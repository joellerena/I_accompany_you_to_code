# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:33:58 2019
"""
import random as ra
acum = 0
juego = 0
contador = 0
while(contador <= 8):
    #print("Lanzamientos:")
    for i in range(1,11):
        dado1 = ra.randint(1,6)
        dado2 = ra.randint(1,6)
        if(dado1 + dado2 == 7):
            acum = acum + 1
    if(acum >= 9):
        contador = contador + 1
        print("Sacaste ",acum," veces 7 en juego ",juego)
    acum = 0
    juego = juego + 1
print("En el juego",juego,"lograste",contador," veces ganar")
