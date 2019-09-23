# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:27:39 2019
"""
arreglo = [1,2,3,4,5,6,7,8,9,10]
print("Toda el arreglo: ")
print(arreglo)
print("Elementos del arreglo: ")
for i in arreglo:
    print(i, end=" ")
print()
print("Usando range..")
print("Índices del arreglo: ")
for i in range(len(arreglo)):
    print(i, end=" ")
print()
print("contenido en arreglo[3]:",arreglo[3])
print("contenido en arreglo[-3]:",arreglo[-3])
print("Longitud del arreglo: ", end=" ")
print(len(arreglo))
print("Usando función list: ")
print("list(range(10))")
print(list(range(10)))
print("list('hola')")
print(list('hola'))
