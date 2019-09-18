# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:03:33 2019
"""
print("LIBRETA ESCOLAR")
print("Asignatura: Programación")
acum, i = (0, 0)
nota, promedio = (0, 0.0)
print("Ingrese las notas a continuación, -99 para finalizar")
print("nota [",(i+1),"]", end=" ")
nota = int(input("Ingrese: "))
while(nota!=-99):
    acum = acum + nota
    i = i + 1
    print("nota [",(i+1),"]", end=" ")
    nota = int(input("Ingrese: "))
if(i>0):
    promedio = acum / i
    print("Promedio: ",promedio)
else:
    print("Finalizó el programa")
