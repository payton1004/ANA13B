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


# ANA13B 채수정점
# 총 7정점 
#   St. No.      Run date
# 1. 001           01-15
# 2. 041           01-28
# 3. 050           01-28
# 4. 061           02-01
# 5. 080           02-01
# 6. 089           02-05
# 7. 103           02-07 

### Winkler 
# 정점 1번
# 20230115_st001.txt_TRT
# 20230115_st001.txt    
# 20230115_st001.txt_ABR
# 정점 41번
# 20230128_st041.txt_TRT
# 20230128_st041.txt    
# 20230128_st041.txt_ABR  
# 정점 50번
# 20230128_st050.txt_TRT
# 20230128_st050.txt    
# 20230128_st050.txt_ABR
# 정점 61번
# 20230201_st061.txt_TRT
# 20230201_st061.txt    
# 20230201_st061.txt_ABR
# 정점 80번
# 20230201_st080.txt_TRT
# 20230201_st080.txt    
# 20230201_st080.txt_ABR
# 정점 89번
# 20230205_st089.txt_TRT
# 20230205_st089.txt    
# 20230205_st089.txt_ABR
# 정점 103번
# 20230207_st103.txt_TRT
# 20230207_st103.txt    
# 20230207_st103.txt_ABR


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
    ax1.set_title('Station '+str(st)+',  ANA13B')

    folder='/Users/jung-ok/work1/ANA13B/plot/Winkler/'
    fname='Depth_profile_Winkler_st'+str(st)+'.png'
    plt.savefig(folder+fname) 
    plt.show()        

### cruise name ; change
# example: ANA13B
print("cruise: cruise name")
cruise = input("cruise = ")        

# Winkler 파일명
# CTD 파일명  
# Winkler 파일명 표기방식을 CTD에 맞추기
txt_files = sorted(glob('/Users/jung-ok/work1/ANA13B/raw_data/Winkler/*st_???.txt'))

old_folder='/Users/jung-ok/work1/ANA13B/raw_data/Winkler/'
new_folder='/Users/jung-ok/work1/ANA13B/raw_data/Winkler/new/'
read_txt_write_csv(txt_files, old_folder, new_folder)


winkler_files =sorted(glob(new_folder+'*.csv'))

# 20230115_st001.csv	
# 20230128_st041.csv
# 20230128_st050.csv	
# 20230201_st061.csv	
# 20230201_st080.csv	
# 20230205_st089.csv	
# 20230207_st103.csv	


###
# 0, 1, 2, 3, 4, 5, 6, 
i = input("i = ")
print(winkler_files[int(i)])

# print("Station Number")
st = input("st = ")
# i=0 ; st='001'
# i=1 ; st='041'
# i=2 ; st='050'
# i=3 ; st='061'
# i=4 ; st='080
# i=5 ; st='089'
# i=6 ; st='103'


dw= pd.read_csv(winkler_files[int(i)], index_col=None)

print("Depth, Max")
print(dw['Depth'].max())

ymin = 0
ymax = int(input("ymax = "))

## ANA13B St.001
## Depth [m] min 0,  max 1500
# ymax=1550 ; ymin=0

## ANA13B St.041
## Depth [m] min 0,  max 282
# ymax=300 ; ymin=0

## ANA13B St.050
## Depth [m] min 0,  max 400
# ymax=425 ; ymin=0

## ANA13B St.061
## Depth [m] min 0,  max 538
# ymax=550 ; ymin=0

## ANA13B St.080
## Depth [m] min 0,  max 532
# ymax=550 ; ymin=0

## ANA13B St.089
## Depth [m] min 0,  max 3570
# ymax=3650 ; ymin=0

## ANA13B St.103
## Depth [m] min 0,  max 632
# ymax=650 ; ymin=0


# if st=='17':
#     dw['Niskin_#'][6:8]=7
#     dw['Niskin_#'][8:10]=9
# elif st=='22':
#     # 닛스킨 번호 틀림 
#     dw['Niskin_#'][8]=10
#     # 병 번호 틀림
#     dw['Bottle_#'][8]=84
#     dw['O2[uM]'][8]=np.nan ; dw['O2[umol/kg]'][8]=np.nan 
#     # 분석순서 뒤바뀜
#     dw['Niskin_#'][17]=20 ; dw['Depth'][17]=15
#     # 병 번호 틀림
#     dw['Bottle_#'][17]=36
#     dw['O2[uM]'][17]=np.nan ; dw['O2[umol/kg]'][17]=np.nan 
#     # 분석순서 뒤바뀜
#     dw['Niskin_#'][18]=18 ; dw['Depth'][18]=34
#     # dw['Station'][dw['Station']==15]=23
# elif st=='34':
#     # NaI NaOH 시약이 1 mL가 아닌 1.5 mL가 들어갔음
#     dw['Vol_Reag']=2.5     
# elif st=='42':
#     dw['O2[umol/kg]'][16]=np.nan   
# # elif st=='084':
# #     dw['Niskin_#'][4:6]=6
# else:
#     pass # do nothing

if st=='041':
    dw['Depth'][0]=282    
else:
    pass # do nothing


plot_depth_profile_winkler(st, dw, ymin, ymax)

print('Done')