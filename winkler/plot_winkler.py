#!/usr/bin/env python
# coding: utf-8

# # Table of Contents

import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress


# sampling stations
#      2, 15, 18, 24, 33
# i = [0, 1, 2, 3, 4]

print("i: index of file list")
i = int(input("i = "))


ctd_files =sorted(glob('/work1/ARA10B/raw_data/ctd/bottle_summary/new/*.csv'))
db = pd.read_csv(ctd_files[i], index_col=None,  parse_dates=[1])
# Rename column
db.rename(columns={"Bottle":"Niskin_#"}, inplace=True)    

# winkler_files =sorted(glob('/work1/ARA10B/raw_data/winkler/new/*.csv'))
# dw= pd.read_csv(winkler_files[i], index_col=None)
# # Rename column
# dw.rename(columns={"Depth":"Depth [salt water, m]"}, inplace=True)    

do_files =sorted(glob('/work1/ARA10B/processed/winkler/*.csv'))
do_table= pd.read_csv(do_files[i], index_col=None)

nn = str(do_table['Station'].unique()[0])

# 1: winkler titrator, 2: winkler 자료를 (온도, 염분)값에 의한 보정,  3: CTD SBE sensor 
# (1-2), (1-3), (2-3)
# 최종적으로 winkler 보정값과 CTD sensor 값을 비교
do_table['winkler-corrected'] = do_table['O2[umol/kg]']-do_table['Oxygen, Winkler [umol/kg]']
do_table['winkler-SBE'] = do_table['O2[umol/kg]']-do_table['Oxygen, SBE 43 [umol/kg]']        
do_table['corrected-SBE'] = do_table['Oxygen, Winkler [umol/kg]'] - do_table[u'Oxygen, SBE 43 [umol/kg]']
    
print(do_table[['Depth [salt water, m]','winkler-corrected','winkler-SBE','corrected-SBE']])

print('plot of Oxygen')
## Oxygen
import matplotlib 
matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})
print('Depth [m]: ')    
print(db['Depth [salt water, m]'].min(), db['Depth [salt water, m]'].max())
deep=float(input('deep= '))
## Oxygen
fig = plt.figure(figsize=(6, 10))
#left, bottom, width, height
ax1= fig.add_axes([0.125, 0.1, 0.8, 0.8]) 

if i==0:
    ax1.set_yscale('linear')
elif i==3:
    ax1.set_yscale('linear')
else:
    ax1.set_yscale('log')   

db.plot(y=u'Depth [salt water, m]',x=u'Oxygen, SBE 43 [umol/kg]', legend=False, ax=ax1, \
 marker='o',mec='darkred', mfc='red', ms=7, mew=0.5, alpha=0.5, ls=':', color='red',clip_on=False, zorder=100, label='Bottle')
do_table.plot(y=u'Depth [salt water, m]',x='Oxygen, Winkler [umol/kg]', legend=False,  ax=ax1, \
 marker='o',mec='darkblue', mfc='blue', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='Winkler')
for k in do_table['Niskin_#'].unique():
    db[db['Niskin_#']==k].plot(y=u'Depth [salt water, m]',x=u'Oxygen, SBE 43 [umol/kg]', legend=False,  ax=ax1, \
    marker='o',mec='firebrick', mfc='darkred', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='')

ax1.legend()

# do_table[do_table['Depth [salt water, m]']==150].plot(y=u'Depth [salt water, m]',x=u'Oxygen, Winkler [umol/kg]',legend=False, 
#        marker='o',markeredgecolor='darkred', markerfacecolor='red',markersize=7,mew=1, alpha=0.5,\
#        linestyle='',color='red', clip_on=False, zorder=100, ax=ax1);

# surface=float(input('surface= '))
if i<4:
    low = db[u'Oxygen, SBE 43 [umol/kg]'].min() - 5
    high = db[u'Oxygen, SBE 43 [umol/kg]'].max() + 5
else:
    low = db[u'Oxygen, SBE 43 [umol/kg]'].min() - 15
    high = db[u'Oxygen, SBE 43 [umol/kg]'].max() + 20

if i==0:
    ax1.set_ylim(0, deep)
elif i==3:
    ax1.set_ylim(0, deep)
else:
    ax1.set_ylim(2e0, deep) 

ax1.set_xlim(low, high)
ax1.set_ylabel('Depth [m]', fontsize=10, weight = 'semibold')
ax1.set_xlabel('O$_2$ [$\mu$mol/kg]', fontsize=10, weight = 'semibold', color='black')
plt.gca().invert_yaxis() 

if i==0:
   st='Station '+'0'+nn+', ARA10B'
   print(st)
   file_name = '/work1/ARA10B/plot/winkler/depth_profile_winkler_ctd_st'+'0'+nn+'.png'
else:
   st='Station '+nn+', ARA10B'
   file_name = '/work1/ARA10B/plot/winkler/depth_profile_winkler_ctd_st'+nn+'.png'

plt.suptitle(st)   
plt.savefig(file_name) 
plt.show()
print('Done')

