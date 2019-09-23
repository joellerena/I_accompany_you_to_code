# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
import numpy as np
matriz11 = np.zeros((5,5))
print("\nmatriz11:")
print(matriz11)

print("\nmatriz11:")
for i in range(len(matriz11)):
    for j in range(len(matriz11[i])):
        if((i==2)and(j%4==0)and(i!=j)):
            matriz11[i][j]=1
        if((i%4==0)and(j==2)and(i!=j)):
            matriz11[i][j]=1
        print(int(matriz11[i][j]), end=" ")
    print()
