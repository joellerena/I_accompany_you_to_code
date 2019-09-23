# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:52:01 2019
"""
try:
    with open("archivo.txt",'r') as f:
        f.write("Llenado, funciona")
except:
    print ("no existe el archivo")