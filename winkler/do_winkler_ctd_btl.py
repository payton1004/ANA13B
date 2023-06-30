import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress

import math

# sampling stations
#      2, 15, 18, 24, 33
# i = [0, 1, 2, 3, 4]

# i=2

# if i==0:
#     print(i)
#     print('linear')
# elif i==3:
#     print(i)
#     print('linear')    
# else:
#     print(i)
#     print('log')    

# *.btl file,  
# Averaged and derived bottle data from .ros file, created by Bottle Summary


btl_files = ['/work1/ARA10B/raw_data/ctd/bottle_summary/tmp/ARA10B02CTD1.btl', 
'/work1/ARA10B/raw_data/ctd/bottle_summary/tmp/ARA10B15CTD1.btl', 
'/work1/ARA10B/raw_data/ctd/bottle_summary/tmp/ARA10B18CTD1.btl', 
'/work1/ARA10B/raw_data/ctd/bottle_summary/tmp/ARA10B24CTD1.btl', 
'/work1/ARA10B/raw_data/ctd/bottle_summary/tmp/ARA10B33CTD1.btl']

# station 
# i=0
print("i: index of file list")
i = int(input("i = "))
# btl=btl_files[i]
db = pd.read_csv(btl_files[i],index_col=None, header=None, delimiter=r"\s+", parse_dates=[1])

# potential temperature: 
# In oceanography, the temperature that a water sample would attain if raised adiabatically to the sea surface.
db.columns = ['Bottle','Date_Time',
              'Scan', 'Time, Elapsed [seconds]', 'Depth [salt water, m]',
              'Salinity, Practical [PSU]', 'Temperature [ITS-90, deg C]', 'Potential Temperature [ITS-90, deg C]',
              'Density [sigma-theta, kg/m^3]', 
              'Pressure, Digiquartz [db]', 'Conductivity [mS/cm]', 'Specific Conductance [uS/cm]',
              'Oxygen, SBE 43 [mg/l]', 'Oxygen, SBE 43 [umol/kg]', 'Oxygen Saturation, Weiss [ml/l]',
              'Beam Attenuation, WET Labs C-Star [1/m]',  'Fluorescence, WET Labs ECO-AFL/FL [mg/m^3]',
              'PAR/Irradiance, Biospherical/Licor', 'Latitude [deg]', 'Longitude [deg]', 
              'Julian Days','Scan, sde', 'Elapsed, sde', 'Depth, sde',
              'Salinity, Practical, sde', 'Temperature, sde', 'Potential Temperature, sde',
              'Density, sde', 
              'Pressure, sde', 'Conductivity, sde', 'Specific Conductance, sde',
              'Oxygen [mg/l], sde', 'Oxygen [umol/kg], sde', 'Weiss [ml/l], sde',
              'Beam Attenuation, sde',  'Fluorescence, sde',
              'PAR/Irradiance, sde', 'Latitude, sde', 'Longitude, sde', 
              'Julian Days, sde']

# for i, column in enumerate(db.columns):
#     print(i+1, column)

# *.asc file,  
# Data portion of .cnv converted data file written in ASCII by ASCII Out.
# *U.asc, *D.asc, *.UD.asc

# *.hdr file
# Header recored when acquiring real-time data (same as header information in data file), 
# or header portion of .cnv converted data file written by ASCII Out. 
# Header includes software version, sensor serial numnbers, instrument configuration, etc.

asc_files =sorted(glob('/work1/ARA10B/raw_data/ctd/*.asc'))

old_folder='/work1/ARA10B/raw_data/ctd/'
new_folder='/work1/ARA10B/raw_data/ctd/new/'

for j in np.arange(len(asc_files)):
    # j=0
    asc=asc_files[j]
    fname= asc.split('/')[5]
#     print fname.split('.')[0]+'.asc'
    df= pd.read_csv(old_folder+fname.split('.')[0]+'.asc', index_col=None, delim_whitespace=True, header=None, skiprows=[0])
    df.columns=['Scan Count', 'Time, Elapsed [seconds]','Depth [salt water, m]', 'Temperature [ITS-90, deg C]', 'Temperature, 2 [ITS-90, deg C]', \
     'Pressure, Digiquartz [db]', 'Conductivity [mS/cm]', 'Conductivity, 2 [mS/cm]', 'Specific Conductance [uS/cm]', 'Oxygen, SBE 43 [mg/l]', \
     'Oxygen, SBE 43 [umol/kg]', 'Oxygen Saturation, Weiss [ml/l]', 'Beam Attenuation, WET Labs C-Star [1/m]', 'Fluorescence, WET Labs ECO-AFL/FL [mg/m^3]',\
     'PAR/Irradiance, Biospherical/Licor', 'Latitude [deg]', 'longitude: Longitude [deg]', 'Julian Days', 'Salinity, Practical [PSU]', \
     'Salinity, Practical, 2 [PSU]', 'Potential Temperature [ITS-90, deg C]', 'Potential Temperature, 2 [ITS-90, deg C]', 'Density [sigma-theta, kg/m^3]', \
     'Density, 2 [sigma-theta, kg/m^3]',    'Sound Velocity [Chen-Millero, m/s]', 'Sound Velocity, 2 [Chen-Millero, m/s]','flag']
    df.to_csv(new_folder+fname.split('.')[0]+'.csv', index=False, na_rep=np.nan)

# files =sorted(glob('/work1/ARA10B/raw_data/ctd/new/*.csv'))

downcast_files = ['/work1/ARA10B/raw_data/ctd/new/ARA10B02CTD1_D.csv', 
'/work1/ARA10B/raw_data/ctd/new/ARA10B15CTD1_D.csv', 
'/work1/ARA10B/raw_data/ctd/new/ARA10B18CTD1_D.csv', 
'/work1/ARA10B/raw_data/ctd/new/ARA10B24CTD1_D.csv', 
'/work1/ARA10B/raw_data/ctd/new/ARA10B33CTD1_D.csv']

upcast_files = ['/work1/ARA10B/raw_data/ctd/new/ARA10B02CTD1_U.csv', 
'/work1/ARA10B/raw_data/ctd/new/ARA10B15CTD1_U.csv', 
'/work1/ARA10B/raw_data/ctd/new/ARA10B18CTD1_U.csv', 
'/work1/ARA10B/raw_data/ctd/new/ARA10B24CTD1_U.csv', 
'/work1/ARA10B/raw_data/ctd/new/ARA10B33CTD1_U.csv']


# i ; station 
# downcast 
dd= pd.read_csv(downcast_files[i], index_col=None)
# upcast
du= pd.read_csv(upcast_files[i], index_col=None)

#### 2nd sensor  - 1st sensor
# du[u'Temperature, 2 [ITS-90, deg C]'] - du[u'Temperature [ITS-90, deg C]']
# du['Density, 2 [sigma-theta, kg/m^3]'] - du['Density [sigma-theta, kg/m^3]']
# du[u'Salinity, Practical, 2 [PSU]'] - du[u'Salinity, Practical [PSU]']
# du[u'Conductivity, 2 [mS/cm]'] - du[u'Conductivity [mS/cm]']
# du['Potential Temperature, 2 [ITS-90, deg C]'] - du['Potential Temperature [ITS-90, deg C]']
# du['Sound Velocity, 2 [Chen-Millero, m/s]'] - du['Sound Velocity [Chen-Millero, m/s]']

# ## plot
# fig, axes = plt.subplots(1, 1, figsize=(5, 10) ,sharex=True)
# dd.plot(y=u'Depth [salt water, m]', x=u'Oxygen, SBE 43 [umol/kg]', sharex=True, ax=axes, label='downcast' , linestyle='-', marker='o', alpha=0.25, ms=5, clip_on=False, zorder=100)
# du.plot(y=u'Depth [salt water, m]', x=u'Oxygen, SBE 43 [umol/kg]',sharex=True,ax=axes, label='upcast', linestyle='-', marker='o', alpha=0.25, ms=5, clip_on=False, zorder=100)
# db.plot(y=u'Depth [salt water, m]', x=u'Oxygen, SBE 43 [umol/kg]',sharex=True,ax=axes, label='bottle', linestyle=' ', marker='o', alpha=0.5, clip_on=False, zorder=100)
# y_min = dd['Depth [salt water, m]'].min() - 5
# y_max = dd['Depth [salt water, m]'].max() + 20
# axes.set_ylim(y_max, y_min)
# plt.show()


# fig, axes = plt.subplots(1, 1, figsize=(5, 10) ,sharex=True)
# # dd.plot(x=u'Depth [salt water, m]', y=u'Salinity, Practical [PSU]', sharex=True, ax=axes, label='downcast' )
# # du.plot(x=u'Depth [salt water, m]', y=u'Salinity, Practical [PSU]',sharex=True,ax=axes, label='upcast')
# dd.plot(y=u'Depth [salt water, m]', x=u'Salinity, Practical [PSU]', sharex=True, ax=axes, label='downcast' , linestyle='-', marker='o', alpha=0.25, ms=5, clip_on=False, zorder=100)
# du.plot(y=u'Depth [salt water, m]', x=u'Salinity, Practical [PSU]',sharex=True,ax=axes, label='upcast', linestyle='-', marker='o', alpha=0.25, ms=5, clip_on=False, zorder=100)
# db.plot(y=u'Depth [salt water, m]', x=u'Salinity, Practical [PSU]',sharex=True,ax=axes, label='bottle', linestyle=' ', marker='o', alpha=0.5, clip_on=False, zorder=100)
# y_min = dd['Depth [salt water, m]'].min() - 5
# y_max = dd['Depth [salt water, m]'].max() + 20
# axes.set_ylim(y_max, y_min)
# plt.show()


# fig, axes = plt.subplots(1, 1, figsize=(5, 10) ,sharex=True)
# # dd.plot(x=u'Depth [salt water, m]', y=u'Potential Temperature [ITS-90, deg C]', sharex=True, ax=axes, label='downcast' )
# # du.plot(x=u'Depth [salt water, m]', y=u'Potential Temperature [ITS-90, deg C]',sharex=True,ax=axes, label='upcast')
# dd.plot(y=u'Depth [salt water, m]', x=u'Potential Temperature [ITS-90, deg C]', sharex=True, ax=axes, label='downcast' , linestyle='-', marker='o', alpha=0.25, ms=5, clip_on=False, zorder=100)
# du.plot(y=u'Depth [salt water, m]', x=u'Potential Temperature [ITS-90, deg C]',sharex=True,ax=axes, label='upcast', linestyle='-', marker='o', alpha=0.25, ms=5, clip_on=False, zorder=100)
# db.plot(y=u'Depth [salt water, m]', x=u'Potential Temperature [ITS-90, deg C]',sharex=True,ax=axes, label='bottle', linestyle=' ', marker='o', alpha=0.5, clip_on=False, zorder=100)
# y_min = dd['Depth [salt water, m]'].min() - 5
# y_max = dd['Depth [salt water, m]'].max() + 20
# axes.set_ylim(y_max, y_min)
# plt.show()


### Winkler Titration 
# output file 
# 1. *.txt
# 2. *.txt_ABR
# 3. *.txt_TRT

winkler_files =sorted(glob('/work1/ARA10B/raw_data/winkler/*st*.txt'))

## bash command 
# sublime /work1/ARA10B/raw_data/winkler/parameter.txt

header = pd.read_csv('/work1/ARA10B/raw_data/winkler/parameter.txt', index_col=None)
header=list(header)+['None']
# ['Cruise', 'Station', 'Cast', 'Niskin', 'Depth', 'Lat', 'Lon', 'Bottle_#', 'Sample_date', 'Run_date', 
# 'Thio_Temp(degC)', 'Thio_Density', 'M(Thio tL)', 'M(Thio 20C)', 'End_Point', 'Vol_KIO3', 'N_KIO3', 
# 'Std_Tit', 'Blk_Tit', 'Vol_Reag', 'Bot_Vol(ml)', 'O2[uM]', 'Draw_Temp(degC)', 'Salinity', 'SW_density', 
# 'O2[umol/kg]', 'uLperst', 'uLoffset', 'slope', 'Speed', 'Wait', 'b', 'm', 'mse1', 'b.1', 'm2', 'mse2', 'None']



dw= pd.read_csv(winkler_files[i], index_col=None, sep='\t', names=header)
nn =str(dw['Station'].unique()[0])


# for i in list(dw['Niskin']):
# #     print i
#     print(i, db[u'Oxygen, SBE 43 [umol/kg]'][db['Bottle']==i].to_list())


print(dw[['Station', 'Depth', 'Niskin', 'O2[uM]', 'O2[umol/kg]']])

# print(dw['Niskin'].unique())
# db[[u'Bottle',u'Depth [salt water, m]']]
# db[u'Depth [salt water, m]'][db[u'Bottle']==2]
# for b in dw['Niskin'].unique():
#     print(b, db[u'Depth [salt water, m]'][db[u'Bottle']==b].to_list())

for b in dw['Niskin'].unique():
    print(b)
    dw['Depth'][dw[u'Niskin']==b]=db[u'Depth [salt water, m]'][db[u'Bottle']==b].to_list()

print(dw[['Station', 'Depth', 'Niskin', 'O2[uM]', 'O2[umol/kg]']])


# station 02
if i==0 : 
    dw['O2[uM]'][0]=np.nan
    dw['O2[umol/kg]'][0]=np.nan
    print(dw[['Station', 'Depth', 'Niskin', 'O2[uM]', 'O2[umol/kg]']])



# ['Scan Count', 'Time, Elapsed [seconds]', 'Depth [salt water, m]', 'Temperature [ITS-90, deg C]', 'Temperature, 2 [ITS-90, deg C]', 
# 'Pressure, Digiquartz [db]', 'Conductivity [mS/cm]', 'Conductivity, 2 [mS/cm]', 'Specific Conductance [uS/cm]', 
# 'Oxygen, SBE 43 [mg/l]', 'Oxygen, SBE 43 [umol/kg]', 'Oxygen Saturation, Weiss [ml/l]', 'Beam Attenuation, WET Labs C-Star [1/m]', 
# 'Fluorescence, WET Labs ECO-AFL/FL [mg/m^3]', 'PAR/Irradiance, Biospherical/Licor', 'Latitude [deg]', 'longitude: Longitude [deg]', 'Julian Days', 
# 'Salinity, Practical [PSU]', 'Salinity, Practical, 2 [PSU]', 'Potential Temperature [ITS-90, deg C]', 'Potential Temperature, 2 [ITS-90, deg C]', 
# 'Density [sigma-theta, kg/m^3]', 'Density, 2 [sigma-theta, kg/m^3]', 'Sound Velocity [Chen-Millero, m/s]', 'Sound Velocity, 2 [Chen-Millero, m/s]', 'flag']

print('plot of Temp')
##### plot of 'Temperature [ITS-90, deg C]'
import matplotlib 
matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})
fig = plt.figure(figsize=(6, 10))
#left, bottom, width, height
ax1= fig.add_axes([0.125, 0.1, 0.8, 0.8]) 

if i==0:
    ax1.set_yscale('linear')
elif i==3:
    ax1.set_yscale('linear')
else:
    ax1.set_yscale('log')     
# ax1.set_yscale('log') 

# plt.axhline(y=0, color='darkgray', alpha=.5, ls='--', lw=2)
du.plot(y=u'Depth [salt water, m]',x=u'Temperature [ITS-90, deg C]',legend=False, ax=ax1, \
 marker='o',mec='darkorange', mfc='orange',ms=7, mew=0.5, alpha=0.75, ls='-',color='orange',clip_on=False, zorder=100, label='Upcast')
dd.plot(y=u'Depth [salt water, m]',x=u'Temperature [ITS-90, deg C]',legend=False, ax=ax1, \
    marker='o',mec='darkkhaki', mfc='khaki',ms=7,mew=0.5, alpha=0.75, ls='-',color='khaki',clip_on=False, zorder=100, label='Downcast')
db.plot(y=u'Depth [salt water, m]',x=u'Temperature [ITS-90, deg C]',legend=False,  ax=ax1, \
    marker='o',mec='darkred', mfc='red', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='Bottle')
print('Depth [m]: ')    
print(dd['Depth [salt water, m]'].min(), dd['Depth [salt water, m]'].max())
# print(dd['Depth [salt water, m]'].max())
# surface=float(input('surface= '))
deep=float(input('deep= '))
# print('Temperature [deg C]: ')    
# print(dd[u'Temperature [ITS-90, deg C]'].min(), dd[u'Temperature [ITS-90, deg C]'].max())
# low=float(input('low= '))
# high=float(input('high= '))
# surface = dd['Depth [salt water, m]'].min() - 2.5
# deep = dd['Depth [salt water, m]'].max() + 2.5
low = dd[u'Temperature [ITS-90, deg C]'].min() - 0.1
high = dd[u'Temperature [ITS-90, deg C]'].max() + 0.1
# max: deep,  min: surface
# ax1.set_ylim(deep, surface)
# ax1.set_ylim(deep, 0)
if i==0:
    ax1.set_ylim(0, deep)
elif i==3:
    ax1.set_ylim(0, deep)
else:
    ax1.set_ylim(2e0, deep) 

ymin, ymax = ax1.get_ylim()
print(ymin, ymax)

ax1.set_xlim(low, high)
ax1.set_ylabel('Depth [m]', fontsize=10, weight = 'semibold')
ax1.set_xlabel('Temperature [$^{\circ}$C]', fontsize=10, weight = 'semibold')
ax1.legend()
plt.gca().invert_yaxis()
if i==0 :
   st='Station '+'0'+nn+', ARA10B'
   file_name = '/work1/ARA10B/plot/winkler/depth_profile_st'+'0'+nn+'_temp.png'
else:
   st='Station '+nn+', ARA10B'
   file_name = '/work1/ARA10B/plot/winkler/depth_profile_st'+nn+'_temp.png'
plt.suptitle(st)   
plt.savefig(file_name) 
# plt.show()

print('plot of salinity')
##### plot of u'Salinity, Practical [PSU]'
fig = plt.figure(figsize=(6, 10))
#left, bottom, width, height
ax1= fig.add_axes([0.125, 0.1, 0.8, 0.8]) 

if i==0:
    ax1.set_yscale('linear')
elif i==3:
    ax1.set_yscale('linear')
else:
    ax1.set_yscale('log')     

# plt.axhline(y=0, color='darkgray', alpha=.5, ls='--', lw=2)

du.plot(y=u'Depth [salt water, m]',x=u'Salinity, Practical [PSU]',legend=False, ax=ax1, \
marker='o',mec='darkorange', mfc='orange',ms=7, mew=0.5, alpha=0.75, ls='-',color='orange',clip_on=False, zorder=100, label='Upcast')

dd.plot(y=u'Depth [salt water, m]',x=u'Salinity, Practical [PSU]',legend=False, ax=ax1, \
marker='o',mec='darkkhaki', mfc='khaki',ms=7,mew=0.5, alpha=0.75, ls='-',color='khaki',clip_on=False, zorder=100, label='Downcast')

db.plot(y=u'Depth [salt water, m]',x=u'Salinity, Practical [PSU]',legend=False,  ax=ax1, \
marker='o',mec='darkred', mfc='red', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='Bottle')

# surface = dd['Depth [salt water, m]'].min() - 2.5
# deep = dd['Depth [salt water, m]'].max() + 2.5
low = dd[u'Salinity, Practical [PSU]'].min() - 0.1
high = dd[u'Salinity, Practical [PSU]'].max() + 0.1

# max: deep,  min: surface
# ax1.set_ylim(deep, surface)
# ax1.set_ylim(deep, 0)
if i==0:
    ax1.set_ylim(0, deep)
elif i==3:
    ax1.set_ylim(0, deep)
else:
    ax1.set_ylim(2e0, deep) 
ax1.set_xlim(low, high)
ax1.set_ylabel('Depth [m]', fontsize=10, weight = 'semibold')
ax1.set_xlabel('Salinity, Practical [PSU]', fontsize=10, weight = 'semibold')
ax1.legend()
plt.gca().invert_yaxis()

if i==0:
   st='Station '+'0'+nn+', ARA10B'
   file_name = '/work1/ARA10B/plot/winkler/depth_profile_st'+'0'+nn+'_salinity.png'
else:
   st='Station '+nn+', ARA10B'
   file_name = '/work1/ARA10B/plot/winkler/depth_profile_st'+nn+'_salinity.png'

plt.suptitle(st)   
plt.savefig(file_name) 
# plt.show()


print('plot of density')
##### plot of u'Density [sigma-theta, kg/m^3]'
fig = plt.figure(figsize=(6, 10))
#left, bottom, width, height
ax1= fig.add_axes([0.125, 0.1, 0.8, 0.8]) 

if i==0:
    ax1.set_yscale('linear')
elif i==3:
    ax1.set_yscale('linear')
else:
    ax1.set_yscale('log')     

# plt.axhline(y=0, color='darkgray', alpha=.5, ls='--', lw=2)

du.plot(y=u'Depth [salt water, m]',x=u'Density [sigma-theta, kg/m^3]',legend=False, ax=ax1, \
marker='o',mec='darkorange', mfc='orange',ms=7, mew=0.5, alpha=0.75, ls='-',color='orange',clip_on=False, zorder=100, label='Upcast')

dd.plot(y=u'Depth [salt water, m]',x=u'Density [sigma-theta, kg/m^3]',legend=False, ax=ax1, \
marker='o',mec='darkkhaki', mfc='khaki',ms=7,mew=0.5, alpha=0.75, ls='-',color='khaki',clip_on=False, zorder=100, label='Downcast')

db.plot(y=u'Depth [salt water, m]',x=u'Density [sigma-theta, kg/m^3]',legend=False,  ax=ax1, \
marker='o',mec='darkred', mfc='red', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='Bottle')

# surface = dd['Depth [salt water, m]'].min() - 2.5
# deep = dd['Depth [salt water, m]'].max() + 2.5
low = dd[u'Density [sigma-theta, kg/m^3]'].min() - 0.1
high = dd[u'Density [sigma-theta, kg/m^3]'].max() + 0.1

# max: deep,  min: surface
# ax1.set_ylim(deep, surface)
# ax1.set_ylim(deep, 0)
if i==0:
    ax1.set_ylim(0, deep)
elif i==3:
    ax1.set_ylim(0, deep)
else:
    ax1.set_ylim(2e0, deep) 
ax1.set_xlim(low, high)
ax1.set_ylabel('Depth [m]', fontsize=10, weight = 'semibold')
ax1.set_xlabel('Density [$\sigma$$_{\\theta}$, kg/m$^{3}$]', fontsize=10, weight = 'semibold')
ax1.legend()
plt.gca().invert_yaxis()

if i==0:
   st='Station '+'0'+nn+', ARA10B'
   file_name = '/work1/ARA10B/plot/winkler/depth_profile_st'+'0'+nn+'_sigma_theta.png'
else:
   st='Station '+nn+', ARA10B'
   file_name = '/work1/ARA10B/plot/winkler/depth_profile_st'+nn+'_sigma_theta.png'

plt.suptitle(st)   
plt.savefig(file_name) 
# plt.show()



print('plot of Oxygen')
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

# plt.axhline(y=0, color='darkgray', alpha=.5, ls='--', lw=2)
# 'O2[umol/kg]'
du[du[u'Oxygen, SBE 43 [umol/kg]']>0].plot(y=u'Depth [salt water, m]',x=u'Oxygen, SBE 43 [umol/kg]',legend=False, ax=ax1, \
 marker='o',mec='darkorange', mfc='orange',ms=7, mew=0.5, alpha=0.75, ls='-',color='orange',clip_on=False, zorder=100, label='Upcast')

dd[dd[u'Oxygen, SBE 43 [umol/kg]']>0].plot(y=u'Depth [salt water, m]',x=u'Oxygen, SBE 43 [umol/kg]',legend=False, ax=ax1, \
 marker='o',mec='darkkhaki', mfc='khaki',ms=7,mew=0.5, alpha=0.75, ls='-',color='khaki',clip_on=False, zorder=100, label='Downcast')

db[db[u'Oxygen, SBE 43 [umol/kg]']>0].plot(y=u'Depth [salt water, m]',x=u'Oxygen, SBE 43 [umol/kg]',legend=False, ax=ax1, \
 marker='o',mec='darkred', mfc='red', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='Bottle')

dw[dw[u'O2[umol/kg]']>0].dropna(subset=['O2[umol/kg]']).plot(y=u'Depth',x=u'O2[umol/kg]',legend=False,  ax=ax1, \
 marker='o',mec='darkblue', mfc='blue', ms=7, mew=0.5, alpha=0.5, ls='', color='olive', clip_on=False, zorder=100, label='Winkler')

for k in dw['Niskin'].unique():
    db[db['Bottle']==k].plot(y=u'Depth [salt water, m]',x=u'Oxygen, SBE 43 [umol/kg]', legend=False,  ax=ax1, \
    marker='o',mec='firebrick', mfc='darkred', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='')

ax1.legend()

# print('Depth [m]: ')    
# print(dd['Depth [salt water, m]'].min(), dd['Depth [salt water, m]'].max())
# surface=float(input('surface= '))
# deep=float(input('deep= '))
# print('Temperature [deg C]: ')    
# print(dd[u'Temperature [ITS-90, deg C]'].min(), dd[u'Temperature [ITS-90, deg C]'].max())
# low=float(input('low= '))
# high=float(input('high= '))
# surface = dd['Depth [salt water, m]'].min() - 2.5
# deep = dd['Depth [salt water, m]'].max() + 2.5
low = dd[u'Oxygen, SBE 43 [umol/kg]'].min() - 0.5
high = dd[u'Oxygen, SBE 43 [umol/kg]'].max() + 0.5
# max: deep,  min: surface
# ax1.set_ylim(deep, surface)
# ax1.set_ylim(deep, 0)
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

# print(i)

if i==0:
   st='Station '+'0'+nn+', ARA10B'
   print(st)
   file_name = '/work1/ARA10B/plot/winkler/depth_profile_st'+'0'+nn+'_DO.png'
else:
   st='Station '+nn+', ARA10B'
   file_name = '/work1/ARA10B/plot/winkler/depth_profile_st'+nn+'_DO.png'

plt.suptitle(st)   
plt.savefig(file_name) 
plt.show()
print('Done')