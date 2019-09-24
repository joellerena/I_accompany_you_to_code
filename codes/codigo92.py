# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# defines el camino donde esta tu archivo de excel
filename = 'planilla.xlsx'
# lectura del archivo excel usando la función pd.read_excel
dataframe = pd.read_excel(filename)
mes = dataframe['Meses']
rubro = dataframe['Rubros']
fig, ax = plt.subplots()
a = 1
b = 12
c = 250
d = 0
# Major ticks every 20, minor ticks every 5
xmajor_ticks = np.arange(a, b, 1)
xminor_ticks = np.arange(a, b, 1)
ymajor_ticks = np.arange(d, c, 50)
yminor_ticks = np.arange(d, c, 10)
ax.set_xticks(xmajor_ticks)
ax.set_xticks(xminor_ticks, minor=True)
ax.set_yticks(ymajor_ticks)
ax.set_yticks(yminor_ticks, minor=True)
# And a corresponding grid
ax.grid(which='major', axis='both', linestyle='--')
ax.plot(mes, rubro, 'm.-') # violeta line with dots
#Encuentro el punto mínimo de la gráfica  
py_rubro = rubro.min()
px_rubro = rubro.idxmin()+1
nota1 = str(px_rubro)+ ' mes = ' +str(py_rubro)+ ' (dólares)'
plt.plot(px_rubro, py_rubro, 'ro')
plt.text(px_rubro+3, py_rubro-0.26, nota1, color='r', fontsize=7)
print(py_rubro, px_rubro)
# Hago un señalización con flecha
pxz=px_rubro
pyz=py_rubro
pxz1=px_rubro+3
pyz1=py_rubro-0.26
flecha = plt.annotate(' ',xy=(pxz, pyz), xycoords='data',
                      xytext=(pxz1, pyz1), fontsize=9,
                      arrowprops=dict(arrowstyle="->",
                                      connectionstyle="arc3,rad=.2"))

# limito el área
plt.xlim(a, b)
plt.ylim(d, c)
plt.grid(True, 'major', 'x', ls='--', lw=.5, c='k', alpha=.3)
plt.legend(loc='best')
plt.xlabel('Meses')
plt.ylabel('Rubros')
plt.suptitle("Planillas de Facturas ENERGY ")
ax.set_title('Energía Eléctrica');
plt.show()
