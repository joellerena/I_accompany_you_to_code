# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:43:44 2019
"""
print("Forma 1")
i = 1
acum1 = 0
while(i<=10):
    acum1 = acum1 + i
    i = i + 1
    print(acum1, end=" ")
print(" ")
print("Forma 2")
acum2 = 0
for i in range (1, 11, 1):
    acum2 = acum2 + i
    print(acum2, end=" ")
