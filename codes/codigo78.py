# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
import numpy as np
matriz9 = np.zeros((5,5))
print("\nmatriz9:")
print(matriz9)

print("\nmatriz9:")
for i in range(len(matriz9)):
    for j in range(len(matriz9[i])):
        if(i == 2):
            matriz9[i][j]=1 # matriz 2
        if(j == 2):
            matriz9[i][j]=1 # matriz 4
        print(int(matriz9[i][j]), end=" ")
    print()
