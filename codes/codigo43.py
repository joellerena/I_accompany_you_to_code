# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:13:12 2019
"""
num1 = 4
## bloque 1
if(num1>=0 and num1<=5):
    print("Buen ingreso")
else:
    print("Mal ingreso")
if(num1<0 or num1>5):
    print("Mal ingreso")
else:
    print("Buen ingreso")    
## bloque 2
if(num1>=-1 and num1<6):
    print("Buen ingreso")
else:
    print("Mal ingreso")
if(num1<=-1 or num1>=6):
    print("Mal ingreso")
else:
    print("Buen ingreso")
    ## bloque 3
if not(num1>-1 and num1<6):
    print("Mal ingreso")
else:
    print("Buen ingreso")
if not(num1<0 or num1>5):
    print("Buen ingreso")
else:
    print("Mal ingreso")  