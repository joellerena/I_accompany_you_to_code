# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
import numpy as np
matriz10 = np.zeros((5,5))
print("\nmatriz10:")
print(matriz10)

print("\nmatriz10:")
for i in range(len(matriz10)):
    for j in range(len(matriz10[i])):
        if((i==j)and(j%2==0)):
            matriz10[i][j]=1 
        if((i==4-j)and(i%2==0)):
            matriz10[i][j]=1 
        print(int(matriz10[i][j]), end=" ")
    print()
