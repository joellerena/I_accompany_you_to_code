# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:56:50 2019
"""
import numpy as np
lista = [4,6,5,10,1,9,8,3,7,2]
maximo = np.amax(lista)
minimo = np.amin(lista)
lista1 = np.sort(lista)
print("Lista: ",lista)
print("Valor máx.",maximo)
print("Valor min.",minimo)
print("Ordena: ",lista1)
print("Sumatoria: ",np.sum(lista))