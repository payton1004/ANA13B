import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress

# cruise=input('cruise= ')
cruise='ARA13B'

### 파일 

# sampling stations, 8 
# ARA13B01, ARA13B17, ARA13B22, ARA13B23, ARA13B34, ARA13B42, ARA13B49, ARA13B55
# i = [0, 1, 2, 3, 4, 5, 6, 7]

## i = 0 (ARA13B, 01)

# station 번호를 15로 잘못 입력됨

# ['O2[umol/kg]']열 [0]행 np.nan 값으로 처리
# niskin # 1, bottle # 1

## i = 1 (ARA13B, 17)

## i = 2 (ARA13B, 22)
# ['O2[umol/kg]']열 [2]행 np.nan 값으로 처리
# niskin # 3, bottle # 4

## i = 3 (ARA13B, 23)

# ['O2[umol/kg]']열 [2]행 np.nan 값으로 처리
# niskin # 16=>14, bottle # 14=>18 변경

#['O2[umol/kg]']열 'Niskin_#'이 1인 행을 np.nan 값으로 처리
# 0, 1, 2행을 drop시킴

## i = 4 (ARA13B, 34)
# 'Niskin_#'[4:6] 4=>6 변경    
# bottle # 6, 7

## i = 5 (ARA13B, 42)

## i = 6 (ARA13B, 49)

## i = 7 (ARA13B, 55)


print("i: index of file list")
i = int(input("i = "))

### CTD sensor (항차명 + 정점번호)
# ARA13B01CTD1.csv	
# ARA13B17CTD1.csv	
# ARA13B22CTD1.csv	
# ARA13B23CTD1.csv	
# ARA13B34CTD1.csv	
# ARA13B42CTD1.csv	
# ARA13B49CTD1.csv	
# ARA13B55CTD1.csv	

ctd_files =sorted(glob('/Users/jung-ok/work1/'+cruise+'/raw_data/ctd/bottle_summary/new/*.csv'))

# cruise=ctd_files[i].split('/')[-1].split('.')[0][:6]
st=ctd_files[i].split('/')[-1].split('.')[0][6:8]

dc = pd.read_csv(ctd_files[i], index_col=None,  parse_dates=[1])

# Rename column
dc.rename(columns={"Bottle":"Niskin_#"}, inplace=True)  

dc[['Niskin_#','Depth [salt water, m]','Oxygen, SBE 43 [umol/kg]']]


### Winkler titrator (파일명: Run date + 정점번호)
# 20220723_st01.csv
# 20220728_st17.csv
# 20220730_st22.csv
# 20220801_st23.csv
# 20220809_st34.csv
# 20220812_st42.csv
# 20220815_st49.csv
# 20220818_st55.csv

winkler_files =sorted(glob('/Users/jung-ok/work1/ARA13B/raw_data/Winkler/new/*.csv'))
dw= pd.read_csv(winkler_files[i], index_col=None)
# Rename column
dw.rename(columns={"Depth":"Depth [salt water, m]"}, inplace=True)   

# for b in dw['Niskin'].unique():
#     print(b)
#     dw['Depth [salt water, m]'][dw[u'Niskin_#']==b]=dc[u'Depth [salt water, m]'][dc[u'Niskin_#']==b].to_list()

### 변경전
# print(dw[['Niskin_#', 'O2[umol/kg]']])
# print(dc[['Niskin_#', 'Depth [salt water, m]']])


### Replace few values in a dataframe column with another value
if st=='17':
    dc['Niskin_#'][0]=1
    dc['Niskin_#'][1]=3
    dc['Niskin_#'][2]=5
    dc['Niskin_#'][3]=7
    dc['Niskin_#'][4]=9
    dc['Niskin_#'][5]=11
    dc['Niskin_#'][6]=13
    dc['Niskin_#'][7]=15
    dc['Niskin_#'][8]=17
    dc['Niskin_#'][9]=19
    dc['Niskin_#'][10]=21
    dc['Niskin_#'][11]=23
    dc['Niskin_#'][12]=24
    # dc['Niskin_#'][13]=14
    # dc['Niskin_#'][14]=15
    # dc['Niskin_#'][15]=16
    # dc['Niskin_#'][16]=17
    # dc['Niskin_#'][17]=18
    # dc['Niskin_#'][18]=19
    # dc['Niskin_#'][19]=20
    # dc['Niskin_#'][20]=21
    # dc['Niskin_#'][21]=22
    # dc['Niskin_#'][22]=23
    # dc['Niskin_#'][23]=24
# elif st=='42':
#     dc['Niskin_#'][0]=1
#     dc['Niskin_#'][1]=2
#     dc['Niskin_#'][3]=3
#     dc['Niskin_#'][4]=4
#     dc['Niskin_#'][5]=5
#     dc['Niskin_#'][6]=6
#     dc['Niskin_#'][7]=7
#     dc['Niskin_#'][8]=8
#     dc['Niskin_#'][9]=9
#     dc['Niskin_#'][10]=10
#     dc['Niskin_#'][11]=11
#     dc['Niskin_#'][12]=12
#     dc['Niskin_#'][13]=13
#     dc['Niskin_#'][14]=14
#     dc['Niskin_#'][15]=15
#     dc['Niskin_#'][16]=16
#     dc['Niskin_#'][17]=17
#     dc['Niskin_#'][18]=18
#     dc['Niskin_#'][19]=19
#     dc['Niskin_#'][20]=20
#     dc['Niskin_#'][21]=21
#     dc['Niskin_#'][22]=22
#     dc['Niskin_#'][2]=23
#     dc['Niskin_#'][23]=24     
else:
    dc['Niskin_#'][0]=1
    dc['Niskin_#'][1]=2
    dc['Niskin_#'][3]=3
    dc['Niskin_#'][4]=4
    dc['Niskin_#'][5]=5
    dc['Niskin_#'][6]=6
    dc['Niskin_#'][7]=7
    dc['Niskin_#'][8]=8
    dc['Niskin_#'][9]=9
    dc['Niskin_#'][10]=10
    dc['Niskin_#'][11]=11
    dc['Niskin_#'][12]=12
    dc['Niskin_#'][13]=13
    dc['Niskin_#'][14]=14
    dc['Niskin_#'][15]=15
    dc['Niskin_#'][16]=16
    dc['Niskin_#'][17]=17
    dc['Niskin_#'][18]=18
    dc['Niskin_#'][19]=19
    dc['Niskin_#'][20]=20
    dc['Niskin_#'][21]=21
    dc['Niskin_#'][22]=22
    dc['Niskin_#'][2]=23
    dc['Niskin_#'][23]=24 

if st=='17':
    dw['Niskin_#'][6:8]=7
    dw['Niskin_#'][8:10]=9
elif st=='22':
    # dw['O2[uM]'][0]=np.nan ; dw['O2[umol/kg]'][0]=np.nan ; dw['End_Point'][0]=np.nan
    # 닛스킨 번호 틀림 
    dw['Niskin_#'][8]=10
    # 병 번호 틀림
    dw['Bottle_#'][8]=84
    dw['O2[uM]'][8]=np.nan ; dw['O2[umol/kg]'][8]=np.nan 
    # 분석순서 뒤바뀜
    dw['Niskin_#'][17]=20 ; dw['Depth [salt water, m]'][17]=15
    # 병 번호 틀림
    dw['Bottle_#'][17]=36
    dw['O2[uM]'][17]=np.nan ; dw['O2[umol/kg]'][17]=np.nan 
    # 분석순서 뒤바뀜
    dw['Niskin_#'][18]=18 ; dw['Depth [salt water, m]'][18]=34
    # dw['Station'][dw['Station']==15]=23
elif st=='34':
    # NaI NaOH 시약이 1 mL가 아닌 1.5 mL가 들어갔음
    dw['Vol_Reag']=2.5     
elif st=='42':
    dw['O2[uM]'][16]=np.nan ; dw['O2[umol/kg]'][16]=np.nan ; dw['End_Point'][16]=np.nan  
# if st=='82':
#     # dw['O2[umol/kg]'][dw.index==16]=np.nan 
#     dw['O2[uM]'][16]=np.nan ; dw['O2[umol/kg]'][16]=np.nan ; dw['End_Point'][16]=np.nan
#     dw['Niskin_#'][dw.index==16]=14
#     dw['Bottle_#'][dw.index==16]=18
# if st=='84':
#     dw['Niskin_#'][4:6]=6    
else:
    pass # do nothing


# # St. 82
# # Niskin_# 1인 행을 제거
# if st=='82':
#     dw['O2[umol/kg]'][dw['Niskin_#']==1]=np.nan
#     dw=dw.drop([0,1,2])   


# if i==0 : 
#      dw['O2[uM]'][18]=np.nan ; dw['O2[umol/kg]'][18]=np.nan ; dw['End_Point'][18]=np.nan
#      dw['O2[uM]'][19]=np.nan ; dw['O2[umol/kg]'][19]=np.nan ; dw['End_Point'][19]=np.nan
# elif i==2 : 
#      dw['O2[uM]'][18]=np.nan ; dw['O2[umol/kg]'][18]=np.nan ; dw['End_Point'][18]=np.nan
#      dw['O2[uM]'][19]=np.nan ; dw['O2[umol/kg]'][19]=np.nan ; dw['End_Point'][19]=np.nan
# elif i==3 : 
#      dw['Niskin_#'][4]=11
#      dw['Bottle_#'][4]=52
#      dw['O2[uM]'][4]=np.nan ; dw['O2[umol/kg]'][4]=np.nan 
#      # 1행 (0) 
#      # 결측값으로 간주, np.nan으로 변경
#      dw['O2[uM]'][0]=np.nan ; dw['O2[umol/kg]'][0]=np.nan ; dw['End_Point'][0]=np.nan
# elif i==4 : 
#     # 17행 (16)
#     # n>30
#     # End point값을 직접 찾아야 함
#     # 결측값으로 간주, np.nan으로 변경
#      dw['O2[uM]'][16]=np.nan ; dw['O2[umol/kg]'][16]=np.nan ; dw['End_Point'][16]=np.nan 
# elif i==5 : 
#     # CTD bottle summary 닛스킨 번호 수정
#      dc['Niskin_#'][3]=9
#      dc['Niskin_#'][4]=10 
#      dc['Niskin_#'][5]=11
#      dc['Niskin_#'][6]=17 
#      dc['Niskin_#'][7]=18
#      dc['Niskin_#'][8]=19  
# elif i==6 : 
#     # 결측값으로 간주, np.nan으로 변경
#      dw['O2[uM]'][0]=np.nan ; dw['O2[umol/kg]'][0]=np.nan ; dw['End_Point'][0]=np.nan 
#     # 8-9행 (7-8)
#     # 뚜껑과 몸체 번호가 다름
#     # 결측값으로 간주, np.nan으로 변경
#      dw['O2[uM]'][7]=np.nan ; dw['O2[umol/kg]'][7]=np.nan ; dw['End_Point'][7]=np.nan 
#      dw['O2[uM]'][8]=np.nan ; dw['O2[umol/kg]'][8]=np.nan ; dw['End_Point'][8]=np.nan        
              
      

### 변경후 
# print(dw[['Niskin_#', 'O2[umol/kg]']])
# print(dc[['Niskin_#', 'Depth [salt water, m]']])

### merge (Winkler titrator, CTD sensor, flask volumes)
winkler=dw[['Station','Niskin_#', 'Bottle_#', 'Std_Tit', 'Blk_Tit','End_Point', \
'Thio_Temp(degC)', 'Thio_Density', 'M(Thio tL)', 'M(Thio 20C)', 'Draw_Temp(degC)', 'Salinity', 'SW_density', 'O2[uM]',  'O2[umol/kg]']]

# ARA13B
ctd=dc[['Date_Time','Latitude [deg]', 'Longitude [deg]', 'Niskin_#', 'Depth [salt water, m]', 'Oxygen, SBE 43 [umol/kg]', \
'Temperature [ITS-90, deg C]', 'Salinity, Practical [PSU]', 'Pressure, Digiquartz [db]']]

# type object => int로 변경
ctd['Niskin_#'] = ctd['Niskin_#'].astype(int, errors='ignore')



do=pd.merge(winkler, ctd, on='Niskin_#')

# Table file that contains flask volumes. 
table = pd.read_csv('/Users/jung-ok/work1/winkler/calibrated volumes of DO bottles at 20degC.txt', index_col=None, sep='\t', header=0)
table.columns=[u'Bottle_#', u'Vol @20C']
table['Bottle_#'] = table['Bottle_#'].astype(int, errors='ignore')
table['Vol @20C'] = table['Vol @20C'].astype(int, errors='ignore')

do_table=pd.merge(do, table, on='Bottle_#')
###


##### blank, standard 적정값 수정
# Volume for Standard/Blank titrating 
# 717.38 => 720.30
# # 5.33 => 720.30
# do_table['Std_Tit'] = 720.30
# do_table['Blk_Tit'] = 2.40
# print(do_table[['Std_Tit','Blk_Tit']])


######### Compare four values ( , , , )
### value directly from Winkler Titrator : 'O2[uM]' 'SW_density' 'O2[umol/kg]'
### checked ; recalculated value from 'Draw_Temp(degC)' of Titration input parameter
### corrected ; recalculated value from  u'Temperature [ITS-90, deg C]' of CTD sensor
### value directly from CTD sensor : u'Oxygen, SBE 43 [umol/kg]'

# Dickson, A. G. (1994), Determination of dissolved oxygen in seawater by Winkler titration. Technical report, WOCE operations manual, WOCE report 68/91 Revision 1 November 1994.
# (Appedix A) Density of sea water
# SMOW - Standard Mean Ocean Water (Craig, 1961) - is pure water with a specified isotopic composition and free of dissolved gases.

### calculate Concentration of Na2S2O3 at Laboratory Temperature , unit: mol/L
# do_table['M(Thio tL)'] ; value directly from Winkler Titrator
# do_table['M(Thio tL), checked'] 

### Concentration of KIO3 at Preparation Temperature
# 몰수 = (질량/몰질량)
# 몰농도 = 몰수 / 부피 
# 0.3567 g,  1L 플라스크에 넣어 최종적으로 0.01 N KIO3를 만든다. (수정: 실제는 2단계로 희석)
# 213.950 g/mol, molar mass of KIO3
# Volume of 1 L at Preparation Temperature
# 'Thio_Temp(degC)' Preparation Temperature (수정)
do_table['M(KIO3 tp)'] = (0.3567 / 213.950) / 1 * (1 + 9.75 * 1E-6*(do_table['Thio_Temp(degC)']-20))

### Volume of bottle top dispenser at Laboratory Temperature
# 9.968 mL, Vol at 20 degC 
# 9.75*1E-6 Thermal expansion coefficient
do_table['V(KIO3 tL)'] = 9.968 * (1 + 9.75 * 1E-6*(do_table['Thio_Temp(degC)']-20))



do_table['M(Thio tL), corrected'] = 6000 * do_table['V(KIO3 tL)'] * do_table['M(KIO3 tp)'] / (do_table['Std_Tit'] - do_table['Blk_Tit'])

# print(do_table[['M(Thio tL), corrected','M(Thio tL)']])


### calculte 'O2[uM]' from 'End_Point'
do_table['O2[mol]']=(do_table['End_Point'] - do_table['Blk_Tit'])*do_table['M(Thio tL)']*1E-6*0.25
do_table['O2[mol], corrected']=(do_table['End_Point'] - do_table['Blk_Tit'])*do_table['M(Thio tL), corrected']*1E-6*0.25

do_table['O2[uM], checked']=((do_table['O2[mol]']-7.6*1E-8)/((do_table[u'Vol @20C']*(1+9.75*1E-6*(do_table[u'Draw_Temp(degC)']-20))-2)*1E-3))*1E6
do_table['O2[uM], corrected']=((do_table['O2[mol], corrected']-7.6*1E-8)/((do_table[u'Vol @20C']*(1+9.75*1E-6*(do_table[u'Temperature [ITS-90, deg C]']-20))-2)*1E-3))*1E6

##### O2[uM]
# do_table[['O2[uM]','O2[uM], checked', 'O2[uM], corrected']]


do_table['SMOW, checked'] =  999.842594 + 6.793952 * 1E-2 * do_table[u'Draw_Temp(degC)'] - 9.095290 * 1E-3 * do_table[u'Draw_Temp(degC)']**2 + 1.001685 * 1E-4 * do_table[u'Draw_Temp(degC)']**3 \
 - 1.120083 * 1E-6 * do_table[u'Draw_Temp(degC)']**4 + 6.536332 * 1E-9 * do_table[u'Draw_Temp(degC)']**5

do_table['A, checked'] =  8.24493 * 1E-1 - 4.0899 * 1E-3 * do_table[u'Draw_Temp(degC)'] + 7.6438 * 1E-5 * do_table[u'Draw_Temp(degC)']**2 - 8.2467 * 1E-7 * do_table[u'Draw_Temp(degC)']**3+ 5.3875 * 1E-9 * do_table[u'Draw_Temp(degC)']**4 

do_table['B, checked'] = -5.72466 * 1E-3 + 1.0227 * 1E-4 * do_table[u'Draw_Temp(degC)']- 1.6546 * 1E-6 * do_table[u'Draw_Temp(degC)']**2  

do_table['C, checked'] = 4.8314 * 1E-4

do_table['SW_density, checked'] = (do_table['SMOW, checked'] + do_table['A, checked']*do_table['Salinity'] + do_table['B, checked']*do_table['Salinity']**1.5 + do_table['C, checked'] * do_table['Salinity']**2)*1E-3


do_table['SMOW, corrected'] = 999.842594 + 6.793952 * 1E-2 * do_table[u'Temperature [ITS-90, deg C]'] - 9.095290 * 1E-3 * do_table[u'Temperature [ITS-90, deg C]']**2 + 1.001685 * 1E-4 * do_table[u'Temperature [ITS-90, deg C]']**3  \
 - 1.120083 * 1E-6 * do_table[u'Temperature [ITS-90, deg C]']**4 + 6.536332 * 1E-9 * do_table[u'Temperature [ITS-90, deg C]']**5

do_table['A, corrected'] = 8.24493 * 1E-1 - 4.0899 * 1E-3 * do_table[u'Temperature [ITS-90, deg C]']+ 7.6438 * 1E-5 * do_table[u'Temperature [ITS-90, deg C]']**2 - 8.2467 * 1E-7 * do_table[u'Temperature [ITS-90, deg C]']**3+ 5.3875 * 1E-9 * do_table[u'Temperature [ITS-90, deg C]']**4 

do_table['B, corrected'] = -5.72466 * 1E-3 + 1.0227 * 1E-4 * do_table[u'Temperature [ITS-90, deg C]']- 1.6546 * 1E-6 * do_table[u'Temperature [ITS-90, deg C]']**2  

do_table['C, corrected'] = 4.8314 * 1E-4

do_table['SW_density, corrected'] = (do_table['SMOW, corrected'] + do_table['A, corrected'] * do_table['Salinity, Practical [PSU]'] + do_table['B, corrected'] * do_table['Salinity, Practical [PSU]']**1.5 + do_table['C, corrected'] * do_table['Salinity, Practical [PSU]']**2)*1E-3

##### SW_density
# do_table[['SW_density','SW_density, checked', 'SW_density, corrected']]
##### 

##### 
do_table['O2[umol/kg], checked']=do_table['O2[uM]']/do_table[u'SW_density']
do_table['O2[umol/kg], corrected']=do_table['O2[uM], corrected']/do_table[u'SW_density, corrected']

##### O2[umol/kg] , Oxygen, SBE 43 [umol/kg]
# do_table[['Depth [salt water, m]','O2[umol/kg]','O2[umol/kg], checked', 'O2[umol/kg], corrected', u'Oxygen, SBE 43 [umol/kg]']]

# co=do_table[['Depth [salt water, m]', 'O2[umol/kg], corrected', u'Oxygen, SBE 43 [umol/kg]']]
# co.columns=['Depth [salt water, m] [m]', 'O2 [umol/kg], Winkler', u'Oxygen, SBE 43 [umol/kg]']
part=do_table[['Station', 'Latitude [deg]', 'Longitude [deg]','Niskin_#', 'Depth [salt water, m]', 'Bottle_#', \
 'Temperature [ITS-90, deg C]', 'Salinity, Practical [PSU]', 'Oxygen, SBE 43 [umol/kg]','O2[umol/kg], corrected', 'O2[umol/kg]','Date_Time']]
part.rename(columns={"O2[umol/kg], corrected":"Oxygen, Winkler [umol/kg]"}, inplace=True)   

# print(part[['Niskin_#', 'Depth [salt water, m]', 'Date_Time']].sort_values(by=['Niskin_#'], ascending=True))

# nn = str(part['Station'].unique()[0])

# folder='/Users/jung-ok/work1/ARA13B/processed/Winkler/'
folder='/Users/jung-ok/work1/'+cruise+'/processed/Winkler/'

# print(i)

# if i==0:
#    file_name = 'dissolved_oxygen_Winkler_CTD_st'+'0'+nn+'.csv'
# else:
#    file_name = 'dissolved_oxygen_Winkler_CTD_st'+nn+'.csv'

file_name = 'dissolved_oxygen_Winkler_CTD_'+cruise+st+'.csv'

# print(folder+file_name)

part.sort_values(by=['Niskin_#'], ascending=True).to_csv(folder+file_name, index=False, na_rep=np.nan, float_format='%g')

# 1: winkler titrator, 2: winkler 자료를 (온도, 염분)값에 의한 보정,  3: CTD SBE sensor 
# (1-2), (1-3), (2-3)
# 최종적으로 winkler 보정값과 CTD sensor 값을 비교
do_table['winkler-corrected'] = do_table['O2[umol/kg]']-do_table['O2[umol/kg], corrected']
do_table['winkler-SBE'] = do_table['O2[umol/kg]']-do_table['Oxygen, SBE 43 [umol/kg]']        
do_table['corrected-SBE'] = do_table['O2[umol/kg], corrected'] - do_table[u'Oxygen, SBE 43 [umol/kg]']
    
# print(do_table[['Depth [salt water, m]','winkler-corrected','winkler-SBE','corrected-SBE']])

# print('plot of Oxygen')
## Oxygen
import matplotlib 
matplotlib.rcParams.update({'font.size': 10, 'font.weight':'bold'})
# print('Depth [m]: ')    
# print(dc['Depth [salt water, m]'].min(), dc['Depth [salt water, m]'].max())
# deep=float(input('deep= '))
## Oxygen
fig = plt.figure(figsize=(7, 8))
#left, bottom, width, height
ax1= fig.add_axes([0.125, 0.1, 0.8, 0.8]) 

dc.plot(y=u'Depth [salt water, m]',x=u'Oxygen, SBE 43 [umol/kg]', legend=False, ax=ax1, \
 marker='o',mec='darkred', mfc='red', ms=7, mew=0.5, alpha=0.5, ls=':', color='red',clip_on=False, zorder=100, label='SBE 43')
do_table.plot(y=u'Depth [salt water, m]',x='O2[umol/kg], corrected', legend=False,  ax=ax1, \
 marker='o',mec='darkblue', mfc='blue', ms=7, mew=0.5, alpha=0.5, ls='', clip_on=False, zorder=100, label='Winkler')

ax1.legend()

low = dc[u'Oxygen, SBE 43 [umol/kg]'].min() - 3
high = dc[u'Oxygen, SBE 43 [umol/kg]'].max() + 15

# ax1.set_xlim(low, high)
ax1.set_ylabel('Depth [m]', fontsize=10, weight = 'semibold')
ax1.set_xlabel('O$_2$ [$\mu$mol/kg]', fontsize=10, weight = 'semibold', color='black')
plt.gca().invert_yaxis() 

# file_name = '/Users/jung-ok/work1/ARA12B/plot/Winkler/depth_profile_winkler_ctd_'+cruise+st+'.png'
file_name = '/Users/jung-ok/work1/'+cruise+'/plot/Winkler/depth_profile_winkler_ctd_'+cruise+st+'.png'

plt.suptitle(cruise+st)   
plt.savefig(file_name) 
plt.show()

print(i)
print('Done')


