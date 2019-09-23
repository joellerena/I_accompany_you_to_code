# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:36:28 2019
"""
import random
import numpy as np
# forma 1 con random
matriz1 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        matriz1[i][j]=random.randrange(10)
print()
# forma 2 con numpy
matriz2 = np.zeros((3,3))
for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        matriz2[i][j]=int(np.random.rand()*10)
        
print("matriz1 \n",matriz1,"\n")
print("matriz2 \n",matriz2,"\n")
matriz3 = matriz1 + matriz2
print("matriz3 (suma) \n",matriz3,"\n")

matriz4 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matriz4)):
    for j in range(len(matriz4[i])):
        matriz4[i][j]= int(matriz1[i][j] + matriz2[i][j])
print("matriz4 (suma) \n",matriz4,"\n")
