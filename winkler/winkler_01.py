import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress

### plotting
import matplotlib 
matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})


# ARA13B 채수정점
# 총 8정점 
#   St. No.      Run date
# 1. 1           07-23
# 2. 17          07-28
# 3. 22          07-30
# 4. 23          08-01
# 5. 34          08-09
# 6. 42          08-12
# 7. 49          08-15 
# 8. 55          08-18

### Winkler 
# 정점 1번
# 20220723_st01.txt_TRT
# 20220723_st01.txt    
# 20220723_st01.txt_ABR
# 정점 17번
# 20220728_st17.txt_TRT
# 20220728_st17.txt    
# 20220728_st17.txt_ABR   
# 정점 22번
# 20220730_st22.txt_TRT
# 20220730_st22.txt    
# 20220730_st22.txt_ABR   
# 정점 23번
# 20220801_st23.txt_TRT
# 20220801_st23.txt    
# 20220801_st23.txt_ABR 
# 정점 34번
# 20220809_st34.txt_TRT
# 20220809_st34.txt    
# 20220809_st34.txt_ABR 
# 정점 42번
# 20220812_st42.txt_TRT
# 20220812_st42.txt    
# 20220812_st42.txt_ABR 
# 정점 49번
# 20220815_st49.txt_TRT
# 20220815_st49.txt    
# 20220815_st49.txt_ABR 
# 정점 55번
# 20220818_st55.txt_TRT
# 20220818_st55.txt    
# 20220818_st55.txt_ABR 

# *.txt 파일을 *.csv 파일로 저장한다.

def read_txt_write_csv(txt_files, old_folder, new_folder):
    for j in np.arange(len(txt_files)):
        txt=txt_files[j]
        fname= txt.split('/')[-1]
        print(j, fname)
        dw= pd.read_csv(old_folder+fname, index_col=None, sep='\t', header=None, parse_dates=[8,9])
        dw.columns = [
        'Cruise',   # ARA13B # %s
        'Station',  # 01 # %d
        'Cast',     # 01 # %d
        'Niskin_#',     # 001  # %d
        'Depth',    # 1169.00 # %.2f
        'Lat',  # lat 
        'Lon',  # lon
        'Bottle_#',     # 047 # %d
        'Sample_date',  # 2020-12-08 # %s
        'Run_date',     # 2020-12-10 # %s
        'Thio_Temp(degC)',  # 24.20 # %.2f
        'Thio_Density',     # 0.99725 # %.5f
        'M(Thio tL)',   # 0.14024 # %.5f
        'M(Thio 20C)',  # 0.14011 # %.5f
        'End_Point',    # 01261.220 # %.3f
        'Vol_KIO3',     # 09.986 # %.3f
        'N_KIO3',   # 0.0100 # %.4f
        'Std_Tit',  # 717.380 # %.3f
        'Blk_Tit',  # 05.330 # %.3f
        'Vol_Reag',     # 002 # %d
        'Bot_Vol(ml)',  # 144.224 # %.3f
        'O2[uM]',   # 308.767 # %.3f
        'Draw_Temp(degC)',  # 00.000 # %.3f 
        'Salinity',     # 30.000 # %.3f
        'SW_density',   # 01.024 # %.3f
        'O2[umol/kg]',  # 301.509 # %.3f
        'uLperst',  # 0.2514 # %.4f
        'uLoffset',     # -1.3 # %.1f
        'slope',    # 4.5 # %.1f
        'Speed',    # 0.7 # %.1f
        'Wait',     # 2147483647# %d 
        'b',    # 220.5862517 # %.2f
        'm',    # -0.1748696 # %.7f
        'mse1',     # 0.0010215 # %.7f
        'b.1',  # 49.4562218 # %.7f
        'm2',   # -0.0391597 # %.7f
        'mse2',     # 0.0001874 # %.7f
        'None'  # nan # %s
        ]
        dw.to_csv(new_folder+fname.split('.')[0]+'.csv', index=False, na_rep=np.nan, float_format='%g')
        print("write")


def plot_depth_profile_winkler(st, dw, ymin, ymax):
    # fig, ax1 = plt.subplots(figsize=(9, 9))
    fig = plt.figure(figsize=(6, 9))
    ax1= fig.add_axes([0.15, 0.1, 0.8, 0.7]) 

    dw.plot(y=u'Depth',x='O2[umol/kg]', legend=False,  ax=ax1, \
 marker='o',mec='darkblue', mfc='blue', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='Winkler')

    ax1.set_ylim(ymax,ymin)
    ax1.set_xlabel('O2 [umol/kg]', fontsize=10, weight = 'semibold', color='black')#color='green'
    ax1.set_ylabel('Depth [m]', fontsize=10, weight = 'semibold')
    ax1.set_title('Station '+str(st)+',  ARA13B')

    folder='/Users/jung-ok/work1/ARA13B/plot/Winkler/'
    fname='Depth_profile_Winkler_st'+str(st)+'.png'
    plt.savefig(folder+fname) 
    plt.show()        

### cruise name ; change
# example: ARA13B
print("cruise: cruise name")
cruise = input("cruise = ")        

# Winkler 파일명
# CTD 파일명  
# Winkler 파일명 표기방식을 CTD에 맞추기
txt_files = sorted(glob('/Users/jung-ok/work1/ARA13B/raw_data/Winkler/*st??.txt'))

old_folder='/Users/jung-ok/work1/ARA13B/raw_data/Winkler/'
new_folder='/Users/jung-ok/work1/ARA13B/raw_data/Winkler/new/'
read_txt_write_csv(txt_files, old_folder, new_folder)


winkler_files =sorted(glob(new_folder+'*.csv'))

# 20220723_st01.csv	
# 20220728_st17.csv
# 20220730_st22.csv	
# 20220809_st34.csv	
# 20220815_st49.csv	
# 20220801_st23.csv	
# 20220812_st42.csv	
# 20220818_st55.csv

###
# 0, 1, 2, 3, 4, 5, 6, 7
i = input("i = ")
print(winkler_files[int(i)])

# print("Station Number")
st = input("st = ")
# i=0 ; st='01'
# i=1 ; st='17'
# i=2 ; st='22'
# i=3 ; st='23'
# i=4 ; st='34'
# i=5 ; st='42'
# i=6 ; st='49'
# i=7 ; st='55'

dw= pd.read_csv(winkler_files[int(i)], index_col=None)

print("Depth, Max")
print(dw['Depth'].max())

ymin = 0
ymax = int(input("ymax = "))

## ARA13B St.01
## Depth [m] min 0,  max 40
# ymax=40 ; ymin=0
## ARA13B St.17
## Depth [m] min 0,  max 242
# ymax=245 ; ymin=0
## ARA13B St.22
## Depth [m] min 0,  max 1429
# ymax=1450 ; ymin=0
## ARA13B St.23
## Depth [m] min 0,  max 2234
# ymax=2250 ; ymin=0
## ARA13B St.34
## Depth [m] min 0,  max 515
# ymax=520 ; ymin=0
## ARA13B St.42
## Depth [m] min 0,  max 1084
# ymax=1100 ; ymin=0
## ARA13B St.49
## Depth [m] min 0,  max 533
# ymax=550 ; ymin=0
## ARA13B St.55
## Depth [m] min 0,  max 2086
# ymax=2100 ; ymin=0


if st=='17':
    dw['Niskin_#'][6:8]=7
    dw['Niskin_#'][8:10]=9
elif st=='22':
    # 닛스킨 번호 틀림 
    dw['Niskin_#'][8]=10
    # 병 번호 틀림
    dw['Bottle_#'][8]=84
    dw['O2[uM]'][8]=np.nan ; dw['O2[umol/kg]'][8]=np.nan 
    # 분석순서 뒤바뀜
    dw['Niskin_#'][17]=20 ; dw['Depth'][17]=15
    # 병 번호 틀림
    dw['Bottle_#'][17]=36
    dw['O2[uM]'][17]=np.nan ; dw['O2[umol/kg]'][17]=np.nan 
    # 분석순서 뒤바뀜
    dw['Niskin_#'][18]=18 ; dw['Depth'][18]=34
    # dw['Station'][dw['Station']==15]=23
elif st=='34':
    # NaI NaOH 시약이 1 mL가 아닌 1.5 mL가 들어갔음
    dw['Vol_Reag']=2.5     
elif st=='42':
    dw['O2[umol/kg]'][16]=np.nan   
# elif st=='084':
#     dw['Niskin_#'][4:6]=6
else:
    pass # do nothing


plot_depth_profile_winkler(st, dw, ymin, ymax)

print('Done')