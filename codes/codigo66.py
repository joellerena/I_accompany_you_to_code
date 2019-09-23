# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:17:41 2019
"""
import numpy as np
matriz1 = np.zeros((3,3))
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        matriz1[i][j]=int(np.random.rand()*10)
print("matriz1 \n",matriz1,"\n")
matriz2 = np.zeros((3,3))
for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        matriz2[i][j]=int(np.random.rand()*10)
print("matriz2 \n",matriz2,"\n")
matriz3 = np.zeros((3,3))
for i in range(len(matriz3)):
    for j in range(len(matriz3[i])):
        for k in range(len(matriz3[i])):
            matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
print("matriz3 (multiplicación) \n",matriz3,"\n")