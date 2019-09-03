# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:29:56 2019
"""
import sys
print("Mensaje para","error", file=sys.stderr, flush=True)
print("Salida desde archivo", file=sys.stdout, flush=True)
print()
print("Mensaje para","error", file=sys.stderr, flush=False)
print("Salida desde archivo", file=sys.stdout, flush=False)