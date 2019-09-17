# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:14:10 2019
"""
num = 1
con = 0
while(num <= 100):
    if(num % 10 == 0):
        print("")
    p = num
    i = 1
    while(i <= p):
        r = p % i
        if (r == 0):
            con = con + 1
        i = i + 1
    if(con <= 2):
        print("\t",p,end=" ")
    con = 0
    i = 0
    num = num + 1
