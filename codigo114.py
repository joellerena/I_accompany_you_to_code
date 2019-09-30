# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:59:08 2019
"""
import random as ra
cantidad = 20
verde = 15
azul = 5
cverde = 0
cazul = 0
intento = 0
objetivo = 0
while(cazul!=azul):
    intento = intento + 1
    if((cverde != verde) or (cazul != azul)):
        bolita = int(ra.randint(1,2))
        if(bolita == 1):
            cazul = cazul + 1
        else:
            cverde = cverde + 1            
    if(cverde == verde):
        bolita = 1;
    else:
        bolita = 2;
print("Cantidad de intentos: ",intento)
print("Bolitas azules sacadas: ",cazul)
print("Bolitas verdes sacadas: ",cverde)
print("De 5 bolitas azules faltantes: ",(azul - cazul))
print("De 15 bolitas verdes faltantes: ",(cantidad - azul - cverde))
