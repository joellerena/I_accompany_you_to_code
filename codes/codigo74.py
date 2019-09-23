# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
matriz5 = [[0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0]]
print("\nmatriz5:")
print(matriz5)

print("\nmatriz5:")
for i in range(len(matriz5)):
    for j in range(len(matriz5[i])):
        matriz5[i][j]=1
        if(i == 0):
            matriz5[i][j]=0
        if(i == 4):
            matriz5[i][j]=0
        if(j == 0):
            matriz5[i][j]=0
        if(j == len(matriz5)-1):
            matriz5[i][j]=0
        print(matriz5[i][j], end=" ")
    print()