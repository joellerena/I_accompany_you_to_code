# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:40:35 2019
"""
diccionario1 = {
        "disco":"¿Cuál es tu Python?",
        "cantante":"Anaconda",
        "album":"Conda y Mini Conda",
        "canciones":"10",
        "productora":"Zoni"
        }
indice = diccionario1.keys()
cantidad = diccionario1.items()
elementos = diccionario1.values()

for indice , elementos in cantidad:
    print(indice + " : " + elementos)


