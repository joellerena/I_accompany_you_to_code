# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:59:08 2019
"""
import numpy as np
import random as ra
matriz=np.zeros((4,4))
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
            matriz[i][j]=int(ra.randint(1,9))
            
print("Números de Lotería")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(int(matriz[i][j]),end="")
    if(i==1):
        print("\n")