# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:32:43 2019
"""
conjunto1 = {
        "Lunes","Martes",
        "Miércoles","Jueves",
        "Viernes","Sábado",
        "Domingo",
        }
conjunto2 = {"Martes", "Jueves"}
print(conjunto1)
print(conjunto2)
for i in conjunto1:
    print(i, end=", ")
print()
print("Intersección: ",conjunto1 & conjunto2)