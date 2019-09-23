# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:56:15 2019
"""
tupla1 = (1,2,3,4,5,6,7,8,9,10)
tupla2 = "192.168.1.1","IP","red"
print("Toda la tupla 1: ")
print(tupla1)
print("Elementos de la tupla 2: ")
for i in tupla2:
    print(i, end=" ")
print()
print("Usando range..")
print("Índices de la tupla 1: ")
for i in range(len(tupla1)):
    print(i, end=" ")
print()
print("contenido en tupla1[3]:",tupla1[3])
print("contenido en tupla2[-3]:",tupla2[-3])
print("Longitud de la tupla 2: ", end=" ")
print(len(tupla2))
algo1, algo2, algo3 = tupla2
print(algo1," ",algo2," ",algo3)