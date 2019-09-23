# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
import numpy as np
matriz12 = np.zeros((5,5))
print("\nmatriz12:")
print(matriz12)

print("\nmatriz12:")
for i in range(len(matriz12)):
    for j in range(len(matriz12[i])):
        matriz12[i][j]=1;
        print(int(matriz12[i][j]), end=" ")
    print()
