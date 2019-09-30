# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:35:07 2019
"""
try:
    f = open("archivo.txt", 'w')
    f.write("prueba")
except:
    print ("error al abrir fichero")
finally:
    if f:
        f.close()

