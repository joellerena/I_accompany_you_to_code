# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:19:26 2019
"""
lista = [0]
i = 0
lista[i] = int(input("Ingrese un número: "))
while(lista[i]>1):
    if(lista[i] % 2 == 0):
        lista.append(lista[i] // 2)
    else:
        lista.append(lista[i] * 3 + 1)
    i = i + 1
print(lista, end=" ")
