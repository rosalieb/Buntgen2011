#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:53:13 2017

@author: Rosalie
"""

#Tentative de reproduction de la Figure 4 de Buntgen et al, 2011

import numpy as np # Clone de Matlab
import matplotlib.pyplot as plt # Librairie graphique

#---------------------------
#Import dataset
import pandas as pd
data=pd.read_csv("~/Desktop/2017.01.10 Github/Buntgen2011/Buntgen2011-climat-europe.csv",
           delim_whitespace=True,
           skipinitialspace=True)

list(data) # To get colnames
x = data['Year']
y1 = data['Buentgen_etal.Science2011_JJA-temp']
y2 = y1.rolling(window=31,center=False).mean()
y3tmp = data['Buentgen_etal.Science2011_JJA-temp-RMSE']
y3 = y3tmp.rolling(window=31,center=False).mean()
y4tmp = data['Buentgen_etal.Science2011_JJA-temp+RMSE']
y4 = y4tmp.rolling(window=31,center=False).mean()
y5tmp = data['Buentgen_etal.Science2011_JClim2006-temp']
y5 = y5tmp.rolling(window=31,center=False).mean()

#---------------------------
#Mise en page plus fine de la figure
from matplotlib import rc
plt.rc("text",usetex=True)
plt.rc("font",family='serif', weight='normal',style='normal')
rc['font.serif'] = ['Times']
#rc['xtick.labelsize'] = 10.
#rc['ytick.labelsize'] = 10.
#rc['axes.labelsize'] = 10.
width = 6.69 # Largeur de la figure
height = width/1.4 # Hauteur de la figure
#---------------------------


fig = plt.figure(figsize = (width,height)) # Pour la dimension de la figure, il faut parler en pouces.

plt.plot(x, y1, color='orange', linewidth=0.6)
plt.plot(x, y2, color='firebrick', linewidth=1.8)
plt.plot(x, y3, color='firebrick', linewidth=1.0)
plt.plot(x, y4, color='firebrick', linewidth=1.0)
plt.plot(x, y5, color='black', linewidth=1.8)
plt.set_ylabel('Temperature Anomalies ($^\circ$C)')
plt.set_xlabel("Temps, $t$")
plt.savefig("BuntgenFig4_1.pdf")
