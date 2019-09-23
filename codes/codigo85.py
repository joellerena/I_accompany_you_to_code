# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 07:54:58 2019
"""
def ruso(lista):
    i = 0
    acum = 0
    while(lista[i]>=1):
        a = lista[i]
        b = lista[i+1]
        if(a%2 == 1):
            acum = acum + b
        lista.append(a//2) #ubica al final
        lista.append(b*2)#ubica al final
        i = i + 2
    return acum

n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))    
resultado = ruso([n1, n2])
print("Respuesta es: ", resultado)