import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress

### Winkler 
# *.txt 파일을 *.csv 파일로 저장한다.
# 정점 01번
# 20230115_st_01.txt_TRT
# 20230115_st_01.txt
# 20230115_st_01.txt_ABR
# 정점 41번
# 정점 50번
# 정점 82번
# 정점 61번
# 정점 80번
# 정점 89번
# 정점 103번

def read_txt_write_csv(txt_files, old_folder, new_folder):
    for j in np.arange(len(txt_files)):
        txt=txt_files[j]
        fname= txt.split('/')[-1]
        print(j, fname)
        dw= pd.read_csv(old_folder+fname, index_col=None, sep='\t', header=None, parse_dates=[8,9])
        dw.columns = [
        'Cruise', 	# ARA12 # %s
        'Station', 	# 021 # %d
        'Cast', 	# 001 # %d
        'Niskin_#', 	# 001  # %d
        'Depth', 	# 1169.00 # %.2f
        'Lat', 	# lat 
        'Lon', 	# lon
        'Bottle_#', 	# 047 # %d
        'Sample_date', 	# 2020-12-08 # %s
        'Run_date', 	# 2020-12-10 # %s
        'Thio_Temp(degC)', 	# 24.20 # %.2f
        'Thio_Density', 	# 0.99725 # %.5f
        'M(Thio tL)', 	# 0.14024 # %.5f
        'M(Thio 20C)', 	# 0.14011 # %.5f
        'End_Point', 	# 01261.220 # %.3f
        'Vol_KIO3', 	# 09.986 # %.3f
        'N_KIO3', 	# 0.0100 # %.4f
        'Std_Tit', 	# 717.380 # %.3f
        'Blk_Tit', 	# 05.330 # %.3f
        'Vol_Reag', 	# 002 # %d
        'Bot_Vol(ml)', 	# 144.224 # %.3f
        'O2[uM]', 	# 308.767 # %.3f
        'Draw_Temp(degC)', 	# 00.000 # %.3f 
        'Salinity', 	# 30.000 # %.3f
        'SW_density', 	# 01.024 # %.3f
        'O2[umol/kg]', 	# 301.509 # %.3f
        'uLperst', 	# 0.2514 # %.4f
        'uLoffset', 	# -1.3 # %.1f
        'slope', 	# 4.5 # %.1f
        'Speed', 	# 0.7 # %.1f
        'Wait', 	# 2147483647# %d 
        'b', 	# 220.5862517 # %.2f
        'm', 	# -0.1748696 # %.7f
        'mse1', 	# 0.0010215 # %.7f
        'b.1', 	# 49.4562218 # %.7f
        'm2', 	# -0.0391597 # %.7f
        'mse2', 	# 0.0001874 # %.7f
        'None'	# nan # %s
        ]
        dw.to_csv(new_folder+fname.split('.')[0]+'.csv', index=False, na_rep=np.nan, float_format='%g')
        print("write")

### cruise name ; change
# example: ANA13B
print("cruise: cruise name")
cruise = input("cruise = ")        

txt_files = sorted(glob('/Users/jung-ok/work1/ANA13B/raw_data/Winkler/*st_**.txt'))

old_folder='/Users/jung-ok/work1/ANA13B/raw_data/Winkler/'
new_folder='/Users/jung-ok/work1/ANA13B/raw_data/Winkler/new/'
read_txt_write_csv(txt_files, old_folder, new_folder)


winkler_files =sorted(glob(new_folder+'*.csv'))

# '/Users/jung-ok/work1/ANA13B/raw_data/Winkler/new/20230115_st_01.csv'
# '/Users/jung-ok/work1/ANA13B/raw_data/Winkler/new/20230128_st_41.csv'
# '/Users/jung-ok/work1/ANA13B/raw_data/Winkler/new/20230128_st_50.csv'
# '/Users/jung-ok/work1/ANA13B/raw_data/Winkler/new/20230201_st_61.csv'
# '/Users/jung-ok/work1/ANA13B/raw_data/Winkler/new/20230201_st_80.csv'
# '/Users/jung-ok/work1/ANA13B/raw_data/Winkler/new/20230205_st_89.csv'
# '/Users/jung-ok/work1/ANA13B/raw_data/Winkler/new/20230207_st_103.csv'

###
i = input("i = ")
print(winkler_files[int(i)])

# print("Station Number")
st = input("st = ")
# i=0 ; st='01'
# i=1 ; st='41'
# i=2 ; st='50'
# i=3 ; st='61'
# i=4 ; st='80'
# i=5 ; st='89'
# i=6 ; st='103'

dw= pd.read_csv(winkler_files[int(i)], index_col=None)

print("Depth, Max")
print(dw['Depth'].max())

ymin = 0
# ymax = input("ymax = ")
ymax = int(input("ymax = "))

## ANA13B St.01
## Depth [m] min 0,  max 1500
# ymax=1550 ; ymin=0

## ANA13B St.41
## Depth [m] min 0,  max 282
# ymax=300 ; ymin=0

## ANA13B St.50
## Depth [m] min 0,  max 400
# ymax=425 ; ymin=0

## ANA13B St.61
## Depth [m] min 0,  max 538
# ymax=550 ; ymin=0

## ANA13B St.80
## Depth [m] min 0,  max 532
# ymax=550 ; ymin=0

## ANA13B St.89
## Depth [m] min 0,  max 3570
# ymax=3650 ; ymin=0

## ANA13B St.103
## Depth [m] min 0,  max 632
# ymax=650 ; ymin=0


# St.023
# dw[dw['Bottle_#']==1]['O2[umol/kg]']
# 0   -14.216
# if st=='023':
#     dw['O2[umol/kg]'][0]=np.nan
# if st=='082':
#     dw['O2[umol/kg]'][0]=np.nan   
# if st=='084':
#     dw['Niskin_#'][4:6]=6
if st=='41':
    dw['Depth'][0]=282    
else:
    pass # do nothing

### plotting
import matplotlib 
matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})

def plot_depth_profile_winkler(st, dw, ymin, ymax):
    # fig, ax1 = plt.subplots(figsize=(9, 9))
    fig = plt.figure(figsize=(6, 9))
    ax1= fig.add_axes([0.15, 0.1, 0.8, 0.7]) 

    dw.plot(y=u'Depth',x='O2[umol/kg]', legend=False,  ax=ax1, \
 marker='o',mec='darkblue', mfc='blue', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='Winkler')

    ax1.set_ylim(ymax,ymin)
    ax1.set_xlabel('O2 [umol/kg]', fontsize=10, weight = 'semibold', color='black')#color='green'
    ax1.set_ylabel('Depth [m]', fontsize=10, weight = 'semibold')
    ax1.set_title('Station '+str(st)+',  ANA13B')

    folder='/Users/jung-ok/work1/ANA13B/plot/Winkler/'
    fname='Depth_profile_Winkler_st'+str(st)+'.png'
    plt.savefig(folder+fname) 
    plt.show()

plot_depth_profile_winkler(st, dw, ymin, ymax)