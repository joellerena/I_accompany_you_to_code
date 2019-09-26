# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:59:08 2019
"""
import numpy as np
import random as ra
matriz=np.zeros((5,5))
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j]=ra.randint(1,10)

print("matriz de aleatorios:\n",matriz)