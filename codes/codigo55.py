# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:18:18 2019
"""
acum = 0
n1 = int(input("Ingrese primer número: "))
nn1 = n1
n2 = int(input("Ingrese segundo número: "))
nn2 = n2
while(n1 >= 1):
    print(n1," ",n2)
    if( n1 % 2 == 1):
        acum = acum + n2
    n1 = n1 // 2
    n2 = n2 * 2
print("\n",nn1," por ",nn2, 
      " es ", (nn1*nn2)," = ", acum)