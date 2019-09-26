# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:59:08 2019
"""
import numpy as np
import random as ra
matriz=np.zeros((5,5))
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if(j==0):
            matriz[i][j]=int(ra.randint(1,15))
        if(j==1):
            matriz[i][j]=int(ra.randint(16,31))
        if(j==2):
            matriz[i][j]=int(ra.randint(31,45))
        if(j==3):
            matriz[i][j]=int(ra.randint(46,60))
        if(j==4):
            matriz[i][j]=int(ra.randint(61,75))
            
print("B\tI\tN\tG\tO\n")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(int(matriz[i][j]),"\t",end=" ")
    print("\n")