# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
matriz6 = [[0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0]]
print("\nmatriz6:")
print(matriz6)

print("\nmatriz6:")
for i in range(len(matriz6)):
    for j in range(len(matriz6[i])):
        if(j == 1):
            matriz6[i][j]=1
        if(j == 3):
            matriz6[i][j]=1
        print(matriz6[i][j], end=" ")
    print()