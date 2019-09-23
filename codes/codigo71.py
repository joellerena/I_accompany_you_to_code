# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
import numpy as np
matriz2 = np.zeros((5,5))
print("\nmatriz2:")
print(matriz2)

print("\nmatriz2:")
for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        if(i == j):
            matriz2[i][j] = 1
        print(int(matriz2[i][j]), end=" ")
    print()
