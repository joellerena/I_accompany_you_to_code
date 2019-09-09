# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:34:09 2019
"""
import math
a = 3 # adyacente a te
b = 4 # opuesto a te
c = 5 # hipotenusa
angulo = 53.13010235415598
h = a / math.cos(angulo * math.pi/180)
print("Hipotenusa: ",h)
identidad = 3 / 5
te = math.acos(identidad)
print("Ángulo: ",te * 180/math.pi)