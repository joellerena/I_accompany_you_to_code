# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:07:44 2019
"""
edad=int(input("Ingrese su edad: "))
if(edad < 0):
    print("eres bebé")
elif (edad < 12):
    print("eres niño")
elif (edad < 18):
    print("menor de edad")
elif (edad < 25):
    print("adolescente")
else: 
    if (edad < 60): 
       print("adulto")
    else:
       print("adulto mayor")
