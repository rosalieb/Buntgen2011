#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:53:13 2017

@author: Rosalie
"""

#Tentative de reproduction de la Figure 4 de Buntgen et al, 2011

import numpy as np # Clone de Matlab
import pylab as py # Clone de Matlab
import matplotlib.pyplot as plt # Librairie graphique

#---------------------------
#Import dataset
import pandas as pd
#dat=pd.read_csv("~/Desktop/2017.01.10 Github/Buntgen2011/Buntgen2011-climat-europe.csv",
#           delim_whitespace=True,
#           skipinitialspace=True)
data=pd.read_excel("~/Desktop/PhD/Formations/2017.01.09 Latex/Github/Buntgen2011/Buntgen2011-climat-europe.xls",
           sheetname="Fig.4 Recons", header=6,
           skiprow=[0,1,2,3,4,5])

list(data) # To get colnames
x = data['Year']
y1 = data['Buentgen_etal.Science2011_JJA-temp']
y2 = y1.rolling(window=31,center=True).mean()
y3tmp = data['Buentgen_etal.Science2011_JJA-temp (-RMSE)']
y3 = y3tmp.rolling(window=31,center=True).mean()
y4tmp = data['Buentgen_etal.Science2011_JJA-temp (+RMSE)']
y4 = y4tmp.rolling(window=31,center=True).mean()
y5tmp = data['Buentgen_etal.Science2011_JClim2006-temp']
y5 = y5tmp.rolling(window=31,center=True).mean()

y6 = data['Buentgen_etal.Science2011_AMJ-precip']
y7 = y6.rolling(window=31,center=True).mean()
y8tmp = data['Buentgen_etal.Science2011_AMJ-precip (-RMSE)']
y8 = y8tmp.rolling(window=31,center=True).mean()
y9tmp = data['Buentgen_etal.Science2011_AMJ-precip (+RMSE)']
y9 = y9tmp.rolling(window=31,center=True).mean()

#---------------------------
#Mise en page plus fine de la figure
from matplotlib import rc
from matplotlib import rcParams
#rc("text",usetex=True)
#rc("font",family='serif', weight='normal',style='normal')
#rcParams['font.serif'] = ['Palatino']
rcParams['xtick.labelsize'] = 10.
rcParams['ytick.labelsize'] = 10.
rcParams['axes.labelsize'] = 10.
width = 6.69 # Largeur de la figure
height = width/1.2 # Hauteur de la figure
#---------------------------

fig = plt.figure(figsize = (width,height)) # Pour la dimension de la figure, il faut parler en pouces.

ax1 = fig.add_subplot(1,1,1) #ligne, colonne, numero du graphe

ax2 = ax1.twinx()

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.set_xlim([-500,2010])
ax1.set_ylim([-300,350])
import matplotlib.patches as patches
ax1.add_patch(patches.Rectangle((280, -350),300,800,color='black'))      # (x,y),width & height
    
ax1.set_xlabel("Year (B.C.E. / C.E.)")
ax1.set_ylabel("Precipitations Total (mm)",ha='left')
ax1.plot(x, y6, color='lightblue', linewidth=0.4)
ax1.plot(x, y7, color='steelblue', linewidth=1.6)
ax1.plot(x, y8, color='steelblue', linewidth=0.8)
ax1.plot(x, y9, color='steelblue', linewidth=0.8)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.set_ylim([-3,7])
ax2.plot(x, y1, color='orange', linewidth=0.4)
ax2.plot(x, y2, color='firebrick', linewidth=1.6)
ax2.plot(x, y3, color='firebrick', linewidth=0.8)
ax2.plot(x, y4, color='firebrick', linewidth=0.8)
ax2.plot(x, y5, color='black', linewidth=1.6)
ax2.set_ylabel("Temperature Anomalies ($^\circ$C)", ha='right')


ax1.set_yticks(np.linspace(50, 350, 7))
ax2.set_yticks(np.linspace(-3, 3, 7))
    
ax2.text(-350, 2.2, 'Celtic Expansion', rotation=90, fontsize=11,ha='center', va='center',style='italic')
ax2.text(-210, 2.2, 'Late\nIron\nAge', fontsize=11,ha='center', va='center',color="darkolivegreen")
ax2.text(-30, 2.2, 'Roman Conquest', rotation=90, fontsize=11,ha='center', va='center',style='italic')
ax2.text(150, 2.2, 'Roman\nEmpire', fontsize=11,ha='center', va='center',color="darkolivegreen")
ax2.text(440, 2.2, 'Migration Period', rotation=90, fontsize=11, color="white",ha='center', va='center',style='italic')
ax2.text(1000, 2.2, 'Medieval Period', fontsize=11,ha='center', va='center',color="darkolivegreen")
ax2.text(1400, 2.2, 'Great Famine', rotation=90, fontsize=11,ha='center', va='center',style='italic')
ax2.text(1480, 2.2, 'Black Death', rotation=90, fontsize=11,ha='center', va='center',style='italic')
ax2.text(1600, 2.2, '30 Years\' War', rotation=90, fontsize=11,ha='center', va='center',style='italic')
ax2.text(1810, 2.2, 'Modern Migration', rotation=90, fontsize=11,ha='center', va='center',style='italic')

"""
def addtext(props):
    plt.text(-410, 1, 'Celtic Expansion', props, rotation=90)
    
    plt.text(1.5, 0.5, 'text 45', props, rotation=45)
    plt.text(2.5, 0.5, 'text 135', props, rotation=135)
    plt.text(3.5, 0.5, 'text 225', props, rotation=225)
    plt.text(4.5, 0.5, 'text -45', props, rotation=-45)
    plt.yticks([0, .5, 1])
    plt.grid(True)
"""

fig.savefig("BuntgenFig4_1.pdf")
