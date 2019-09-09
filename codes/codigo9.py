# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:01:54 2019
"""
palabras = "Mi amiga María Cristina"
numero = 19
todo = "{:>28}".format("Mi amigo Sebastián")
print(todo)
print( "{:>28}".format(palabras) ) 
print( "{:28}".format(palabras), end="")
print("sigue")
print( "{:^28}".format(palabras) )
print( "{:.8}".format(palabras) )
palabras = "Mi amiga María Cristina"
otra_forma = f"Hola {palabras}"
print(otra_forma)