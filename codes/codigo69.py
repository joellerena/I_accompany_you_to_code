# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
import numpy as np
matriz1 = np.zeros((5,5))
print("\nmatriz1:")
print(matriz1)

print("\nmatriz1:")
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
            print(int(matriz1[i][j]), end=" ")
    print()
