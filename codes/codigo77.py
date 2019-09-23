# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
matriz8 = [[0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0]]
print("\nmatriz8:")
print(matriz8)

print("\nmatriz8:")
for i in range(len(matriz8)):
    for j in range(len(matriz8[i])):
        if(i == j):
            matriz8[i][j]=1 # matriz 2
        if(j == 4-i):
            matriz8[i][j]=1 # matriz 4
        print(matriz8[i][j], end=" ")
    print()