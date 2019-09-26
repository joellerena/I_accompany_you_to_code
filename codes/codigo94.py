# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:47:46 2019
"""
import threading as th
import time as tiempo
import datetime as dt
class Proceso(th.Thread):
    def run(self):
        ahora = dt.datetime.now()
        print("{} ¡Inicia!".format(self.getName()))   
        print("en el tiempo: %s" % ahora)           
        tiempo.sleep(2)
        luego = dt.datetime.now()                   
        print("{} ¡Terminé!".format(self.getName())) 
        print("---> en el tiempo: %s" % luego)

         
def main():
    for i in range(4):                                     
        proceso = Proceso(name = "Thread-{}".format(i+1))  
        proceso.start()                                   
        tiempo.sleep(.5)  
                                   
if __name__ == '__main__':main()