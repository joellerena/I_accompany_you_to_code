# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:15:26 2019
"""
print("LIBRETA ESCOLAR")
print("Asignatura: Programación")
acum = 0 #acumulador
i = 0    #incrementador o contador
promedio = 0.0
while(i<3):
    print("nota [",(i+1),"]", end=" ")
    nota = int(input("Ingrese: "))
    acum = acum + nota
    i = i + 1
promedio = acum / i
print("Promedio: ",promedio)
