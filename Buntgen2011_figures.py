#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:53:13 2017

@author: Rosalie
"""

#Tentative de reproduction de la Figure 4 de Buntgen et al, 2011

import numpy as np # Clone de Matlab
import matplotlib.pyplot as plt # Librairie graphique

#--------------------
#Import dataset
import pandas as pd
data=pd.read_csv("~/Desktop/2017.01.10 Github/Buntgen2011/Buntgen2011-climat-europe.csv",
           delim_whitespace=True,
           skipinitialspace=True)

list(data) # To get colnames
x = data['Year']
y1 = data['Buentgen_etal.Science2011_JJA-temp']


plt.rc("text",usetex=True)

plt.plot(x, y1, color='navajowhite')
#plt.ylabel('some numbers')
plt.savefig("BuntgenFig4_1.pdf")