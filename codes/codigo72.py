# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
matriz3 = [[0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0]]
print("\nmatriz3:")
print(matriz3)

print("\nmatriz3:")
for i in range(len(matriz3)):
    for j in range(len(matriz3[i])):
        if(i == 0):
            matriz3[i][j]=1
        if(i == 4):
            matriz3[i][j]=1
        if(j == 0): 
            matriz3[i][j]=1
        if(j == len(matriz3)-1):
            matriz3[i][j]=1
        print(matriz3[i][j], end=" ")
    print()