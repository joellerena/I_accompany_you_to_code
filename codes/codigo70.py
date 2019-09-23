# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
matriz2 = [[0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0]]
print("\nmatriz2:")
print(matriz2)

print("\nmatriz2:")
for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        if(i == j):
            matriz2[i][j] = 1
        print(matriz2[i][j], end=" ")
    print()