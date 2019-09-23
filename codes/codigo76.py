# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
matriz7 = [[0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0],[0,0,0,0,0],
           [0,0,0,0,0]]
print("\nmatriz7:")
print(matriz7)

print("\nmatriz7:")
for i in range(len(matriz7)):
    for j in range(len(matriz7[i])):
        if(i == 1):
            matriz7[i][j]=1
        if(i == 3):
            matriz7[i][j]=1
        print(matriz7[i][j], end=" ")
    print()