# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:59:08 2019
"""
import random as ra
ganador = 3
gana_usuario = 0
gana_pc = 0
intento = 0
empate = 0
while((gana_usuario != ganador) and (gana_pc != ganador)):
    intento = intento + 1
    pc = ra.randint(1,3)
    print("\nEcoja: ")
    print("1.- Piedra")
    print("2.- Papel")
    print("3.- Tijera")
    usuario = int(input("Ingrese 1, 2 o 3: "))
    if((usuario == 1) and (pc == 3)):
        gana_usuario+=1
    else:
        if((usuario == 2) and (pc == 1)):
            gana_usuario+=1
        else:
            if((usuario == 3) and (pc == 2)):
                gana_usuario+=1
            else:
                if(usuario == pc):
                    empate+=1
                else:
                    gana_pc+=1
    print("Usuario: ",usuario,"PC: ",pc)
print("\nCantidad de intentos: ",intento)
print("Empates: ",empate)
print("Gana usuario: ",gana_usuario)
print("Gana pc: ",gana_pc)
if(gana_pc>gana_usuario):
    print("GANA PC!!!")
else:
    print("GANA USUARIO!!!")
