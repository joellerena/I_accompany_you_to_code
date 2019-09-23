# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:15:01 2019
"""
n1 = [0]
n2 = [0]
i = 0
acum = 0
n1[i] = int(input("Ingrese primer número: "))
n2[i] = int(input("Ingrese segundo número: "))
while(n1[i]>=1):
    print(n1[i]," ",n2[i])
    if(n1[i] % 2 == 1):
        acum = acum + n2[i]
    n1.append(n1[i] // 2)
    n2.append(n2[i] * 2)
    i = i + 1
print("\n",n1[0],"por",n2[0],
      "es",(n1[0]*n2[0]),"=",acum)
