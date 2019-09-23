# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:33:53 2019
"""
import pandas as pd
lista = ["Do","Re","Mi","Fa","Sol","La","Si"]
index = [1,2,3,4,5,6,7]
serie = pd.Series(lista,index)
print("Presenta: \n%s" % serie)