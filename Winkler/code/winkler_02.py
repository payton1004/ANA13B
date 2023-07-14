import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress

# cruise=input('cruise= ')
cruise='ANA13B'

### 파일 

# sampling stations, 7개 
# AN13B001, ANA13B041, ANA13B050, ANA13B061, ANA13B080, ANA13B089, ANA13B103
# i = [0, 1, 2, 3, 4, 5, 6]


## i = 0 (ANA13B, 001)

## i = 1 (ANA13B, 041)
# 'Depth'[0] 00.00=>282.00 변경  

## i = 2 (ANA13B, 050)

## i = 3 (ANA13B, 061)

## i = 4 (ANA13B, 080)
# 7행을 drop함
# niskin # 12, bottle # 71

## i = 5 (ANA13B, 089)

## i = 6 (ANA13B, 103)
# n > 30
# ['O2[umol/kg]']열 [15]행 np.nan 값으로 처리  
# niskin # 24, bottle # 24



print("i: index of file list")
i = int(input("i = "))

### CTD sensor (항차명 + 정점번호)
# ANA13B001CTD1.csv	
# ANA13B041CTD1.csv	
# ANA13B050CTD1.csv	
# ANA13B061CTD1.csv	
# ANA13B080CTD1.csv	
# ANA13B089CTD1.csv	
# ANA13B103CTD1.csv	


ctd_files =sorted(glob('/Users/jung-ok/work1/'+cruise+'/raw_data/CTD/LAB/bottle_summary/new/*.csv'))

# cruise=ctd_files[i].split('/')[-1].split('.')[0][:6]
st=ctd_files[i].split('/')[-1].split('.')[0][6:9]

dc = pd.read_csv(ctd_files[i], index_col=None,  parse_dates=[1])

# Rename column
dc.rename(columns={"Bottle":"Niskin_#"}, inplace=True)  

dc[['Niskin_#','Depth [salt water, m]','Oxygen, SBE 43 [umol/kg]']]


### Winkler titrator (파일명: Run date + 정점번호)
# 20230115_st_001.csv
# 20230128_st_041.csv
# 20230128_st_050.csv
# 20230201_st_061.csv
# 20230201_st_080.csv
# 20230205_st_089.csv
# 20230207_st_103.csv


winkler_files =sorted(glob('/Users/jung-ok/work1/ANA13B/raw_data/Winkler/new/*.csv'))
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
# dc['Niskin_#'][0]=1
# dc['Niskin_#'][1]=2
# dc['Niskin_#'][3]=3
# dc['Niskin_#'][4]=4
# dc['Niskin_#'][5]=5
# dc['Niskin_#'][6]=6
# dc['Niskin_#'][7]=7
# dc['Niskin_#'][8]=8
# dc['Niskin_#'][9]=9
# dc['Niskin_#'][10]=10
# dc['Niskin_#'][11]=11
# dc['Niskin_#'][12]=12
# dc['Niskin_#'][13]=13
# dc['Niskin_#'][14]=14
# dc['Niskin_#'][15]=15
# dc['Niskin_#'][16]=16
# dc['Niskin_#'][17]=17
# dc['Niskin_#'][18]=18
# dc['Niskin_#'][19]=19
# dc['Niskin_#'][20]=20
# dc['Niskin_#'][21]=21
# dc['Niskin_#'][22]=22
# dc['Niskin_#'][2]=23
# dc['Niskin_#'][23]=24 

if st=='041':
    dw['Depth [salt water, m]'][0] = 282
elif st=='103':
    dw['O2[umol/kg]'][15] = np.nan    
 
           
      

### 변경후 
# print(dw[['Niskin_#', 'O2[umol/kg]']])
# print(dc[['Niskin_#', 'Depth [salt water, m]']])

### merge (Winkler titrator, CTD sensor, flask volumes)
winkler=dw[['Station','Niskin_#', 'Bottle_#', 'Std_Tit', 'Blk_Tit','End_Point', \
'Thio_Temp(degC)', 'Thio_Density', 'M(Thio tL)', 'M(Thio 20C)', 'Draw_Temp(degC)', 'Salinity', 'SW_density', 'O2[uM]',  'O2[umol/kg]']]

# ANA13B
ctd=dc[['Date_Time','Latitude [deg]', 'Longitude [deg]', 'Niskin_#', 'Depth [salt water, m]', 'Oxygen, SBE 43 [umol/kg]', \
'Temperature [ITS-90, deg C]', 'Potential Temperature [ITS-90, deg C]', 'Salinity, Practical [PSU]', 'Pressure, Digiquartz [db]']]

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



do_table['M(Thio tL), checked'] = 6000 * do_table['V(KIO3 tL)'] * do_table['M(KIO3 tp)'] / (do_table['Std_Tit'] - do_table['Blk_Tit'])
do_table['M(Thio tL), corrected'] = 6000 * do_table['V(KIO3 tL)'] * do_table['M(KIO3 tp)'] / (do_table['Std_Tit'] - do_table['Blk_Tit'])
# print(do_table[['M(Thio tL), corrected','M(Thio tL)']])


### calculte 'O2[uM]' from 'End_Point'
do_table['O2[mol], checked']=(do_table['End_Point'] - do_table['Blk_Tit'])*do_table['M(Thio tL), checked']*1E-6*0.25
do_table['O2[mol], corrected']=(do_table['End_Point'] - do_table['Blk_Tit'])*do_table['M(Thio tL), corrected']*1E-6*0.25

# Temperature
do_table['O2[uM], checked']=((do_table['O2[mol], checked']-7.6*1E-8)/((do_table[u'Vol @20C']*(1+9.75*1E-6*(do_table[u'Draw_Temp(degC)']-20))-2)*1E-3))*1E6
do_table['O2[uM], corrected']=((do_table['O2[mol], corrected']-7.6*1E-8)/((do_table[u'Vol @20C']*(1+9.75*1E-6*(do_table[u'Temperature [ITS-90, deg C]']-20))-2)*1E-3))*1E6

##### O2[uM]
# do_table[['O2[uM]','O2[uM], checked', 'O2[uM], corrected']]

# checked
# rho_w ; density of pure water, [kg/m3]
do_table['SMOW, checked'] =  999.842594 + 6.793952 * 1E-2 * do_table[u'Draw_Temp(degC)'] - 9.095290 * 1E-3 * do_table[u'Draw_Temp(degC)']**2 + 1.001685 * 1E-4 * do_table[u'Draw_Temp(degC)']**3 \
 - 1.120083 * 1E-6 * do_table[u'Draw_Temp(degC)']**4 + 6.536332 * 1E-9 * do_table[u'Draw_Temp(degC)']**5

do_table['A, checked'] =  8.24493 * 1E-1 - 4.0899 * 1E-3 * do_table[u'Draw_Temp(degC)'] + 7.6438 * 1E-5 * do_table[u'Draw_Temp(degC)']**2 - 8.2467 * 1E-7 * do_table[u'Draw_Temp(degC)']**3+ 5.3875 * 1E-9 * do_table[u'Draw_Temp(degC)']**4 

do_table['B, checked'] = -5.72466 * 1E-3 + 1.0227 * 1E-4 * do_table[u'Draw_Temp(degC)']- 1.6546 * 1E-6 * do_table[u'Draw_Temp(degC)']**2  

do_table['C, checked'] = 4.8314 * 1E-4

do_table['sigma, checked'] = (do_table['SMOW, checked'] + do_table['A, checked']*do_table['Salinity'] + do_table['B, checked']*do_table['Salinity']**1.5 + do_table['C, checked'] * do_table['Salinity']**2)*1E-3

do_table['Pressure [b], checked'] = do_table['Pressure, Digiquartz [db]'] / 10

do_table['kw, checked'] = 19652.21 + 148.4206 * do_table['Draw_Temp(degC)'] - 2.327105 * do_table['Draw_Temp(degC)']**2 + 1.360477E-2 * do_table['Draw_Temp(degC)']**3 - 5.155288E-5 * do_table['Draw_Temp(degC)']**4

do_table['aw, checked'] = 3.239908 + 1.43713E-3 * do_table['Draw_Temp(degC)'] + 1.16092E-4 * do_table['Draw_Temp(degC)']**2 - 5.77905E-7 * do_table['Draw_Temp(degC)']**3 - 2.54673E-9 * do_table['Draw_Temp(degC)']**4

do_table['bw, checked'] = 8.50935E-5 - 6.12293E-6 * do_table['Draw_Temp(degC)'] + 5.2787E-8 * do_table['Draw_Temp(degC)']**2

FQ0 = 54.6746
FQ1 = - 0.603459


do_table['k, checked'] = do_table['kw, checked'] \
+ (FQ0 + FQ1 * do_table['Draw_Temp(degC)'] + 1.09987E-2 * do_table['Draw_Temp(degC)']**2 - 6.1670E-5 * do_table['Draw_Temp(degC)']**3) * do_table['Salinity'] \
+ (7.944E-2 + 1.6483E-2* do_table['Draw_Temp(degC)'] - 5.3009E-4 * do_table['Draw_Temp(degC)']**2) * do_table['Salinity']**1.5 \
+ (do_table['aw, checked'] + (2.2838E-3 - 1.0981E-5 * do_table['Draw_Temp(degC)'] - 1.6078E-6 * do_table['Draw_Temp(degC)']**2) * do_table['Salinity'] \
+ (1.91075E-4 * do_table['Salinity']**1.5)) * do_table['Pressure [b], checked'] \
+ (do_table['bw, checked'] + (- 9.9348E-7 + 2.0816E-8 * do_table['Draw_Temp(degC)'] + 9.1697E-10 * do_table['Draw_Temp(degC)']**2) * do_table['Salinity']) * do_table['Pressure [b], checked']**2 

do_table['val, checked'] = 1 - do_table['Pressure [b], checked']/do_table['k, checked']

do_table['sigma_p, checked'] = do_table['sigma, checked']/do_table['val, checked'] - 1000

# corrected
do_table['SMOW, corrected'] = 999.842594 + 6.793952 * 1E-2 * do_table[u'Temperature [ITS-90, deg C]'] - 9.095290 * 1E-3 * do_table[u'Temperature [ITS-90, deg C]']**2 + 1.001685 * 1E-4 * do_table[u'Temperature [ITS-90, deg C]']**3  \
 - 1.120083 * 1E-6 * do_table[u'Temperature [ITS-90, deg C]']**4 + 6.536332 * 1E-9 * do_table[u'Temperature [ITS-90, deg C]']**5

do_table['A, corrected'] = 8.24493 * 1E-1 - 4.0899 * 1E-3 * do_table[u'Temperature [ITS-90, deg C]']+ 7.6438 * 1E-5 * do_table[u'Temperature [ITS-90, deg C]']**2 - 8.2467 * 1E-7 * do_table[u'Temperature [ITS-90, deg C]']**3+ 5.3875 * 1E-9 * do_table[u'Temperature [ITS-90, deg C]']**4 

do_table['B, corrected'] = -5.72466 * 1E-3 + 1.0227 * 1E-4 * do_table[u'Temperature [ITS-90, deg C]']- 1.6546 * 1E-6 * do_table[u'Temperature [ITS-90, deg C]']**2  

do_table['C, corrected'] = 4.8314 * 1E-4

do_table['sigma, corrected'] = (do_table['SMOW, corrected'] + do_table['A, corrected'] * do_table['Salinity, Practical [PSU]'] + do_table['B, corrected'] * do_table['Salinity, Practical [PSU]']**1.5 + do_table['C, corrected'] * do_table['Salinity, Practical [PSU]']**2)*1E-3

do_table['Pressure [b], corrected'] = do_table['Pressure, Digiquartz [db]'] / 10

do_table['kw, corrected'] = 19652.21 + 148.4206 * do_table[u'Temperature [ITS-90, deg C]'] - 2.327105 * do_table[u'Temperature [ITS-90, deg C]']**2 + 1.360477E-2 * do_table[u'Temperature [ITS-90, deg C]']**3 - 5.155288E-5 * do_table[u'Temperature [ITS-90, deg C]']**4

do_table['aw, corrected'] = 3.239908 + 1.43713E-3 * do_table['Temperature [ITS-90, deg C]'] + 1.16092E-4 * do_table['Temperature [ITS-90, deg C]']**2 - 5.77905E-7 * do_table['Temperature [ITS-90, deg C]']**3 - 2.54673E-9 * do_table['Temperature [ITS-90, deg C]']**4

do_table['bw, corrected'] = 8.50935E-5 - 6.12293E-6 * do_table['Temperature [ITS-90, deg C]'] + 5.2787E-8 * do_table['Temperature [ITS-90, deg C]']**2

do_table['k, checked'] = do_table['kw, checked'] \
+ (FQ0 + FQ1 * do_table['Draw_Temp(degC)'] + 1.09987E-2 * do_table['Draw_Temp(degC)']**2 - 6.1670E-5 * do_table['Draw_Temp(degC)']**3) * do_table['Salinity'] \
+ (7.944E-2 + 1.6483E-2 * do_table['Draw_Temp(degC)'] - 5.3009E-4 * do_table['Draw_Temp(degC)']**2) * do_table['Salinity']**1.5 \
+ (do_table['aw, checked'] + (2.2838E-3 - 1.0981E-5 * do_table['Draw_Temp(degC)'] - 1.6078E-6 * do_table['Draw_Temp(degC)']**2) * do_table['Salinity'] \
+ (1.91075E-4 * do_table['Salinity']**1.5)) * do_table['Pressure [b], checked'] \
+ (do_table['bw, checked'] + (- 9.9348E-7 + 2.0816E-8 * do_table['Draw_Temp(degC)'] + 9.1697E-10 * do_table['Draw_Temp(degC)']**2) * do_table['Salinity']) * do_table['Pressure [b], checked']**2 

do_table['k, corrected'] = do_table['kw, corrected'] \
+ (54.6746 - 0.603459 * do_table['Temperature [ITS-90, deg C]'] + 1.09987E-2 * do_table['Temperature [ITS-90, deg C]']**2 - 6.1670E-5 * do_table['Temperature [ITS-90, deg C]']**3) * do_table['Salinity'] \
+ (7.944E-2 + 1.6483E-2 * do_table['Temperature [ITS-90, deg C]'] - 5.3009E-4 * do_table['Temperature [ITS-90, deg C]']**2) * do_table['Salinity']**1.5 \
+ (do_table['aw, checked'] + (2.2838E-3 - 1.0981E-5 * do_table['Temperature [ITS-90, deg C]'] - 1.6078E-6 * do_table['Temperature [ITS-90, deg C]']**2) * do_table['Salinity'] \
+ (1.91075E-4 * do_table['Salinity']**1.5)) * do_table['Pressure [b], checked']\
+ (do_table['bw, checked'] + (- 9.9348E-7 + 2.0816E-8 * do_table['Temperature [ITS-90, deg C]'] + 9.1697E-10 * do_table['Temperature [ITS-90, deg C]']**2)* do_table['Salinity']) * do_table['Pressure [b], checked']**2

do_table['val, corrected'] = 1 - do_table['Pressure [b], corrected']/do_table['k, corrected']

do_table['sigma_p, corrected'] = do_table['sigma, corrected']/do_table['val, corrected'] - 1000



##### SW_density
# do_table[['SW_density','sigma_p, checked', 'sigma_p, corrected']]
##### 

##### 
# do_table['O2[umol/kg], checked']=do_table['O2[uM]']/do_table[u'SW_density']
# do_table['O2[umol/kg], corrected']=do_table['O2[uM], corrected']/do_table[u'SW_density, corrected']
do_table['O2[umol/kg], checked']=do_table['O2[uM], checked']/(do_table[u'sigma_p, checked']+1000)
do_table['O2[umol/kg], corrected']=do_table['O2[uM], corrected']/(do_table[u'sigma_p, corrected']+1000)

##### O2[umol/kg] , Oxygen, SBE 43 [umol/kg]
# do_table[['Depth [salt water, m]','O2[umol/kg]','O2[umol/kg], checked', 'O2[umol/kg], corrected', u'Oxygen, SBE 43 [umol/kg]']]

# co=do_table[['Depth [salt water, m]', 'O2[umol/kg], corrected', u'Oxygen, SBE 43 [umol/kg]']]
# co.columns=['Depth [salt water, m] [m]', 'O2 [umol/kg], Winkler', u'Oxygen, SBE 43 [umol/kg]']
part=do_table[['Station', 'Latitude [deg]', 'Longitude [deg]','Niskin_#', 'Depth [salt water, m]', 'Pressure, Digiquartz [db]', 'Bottle_#', \
 'Temperature [ITS-90, deg C]', 'Potential Temperature [ITS-90, deg C]', 'Salinity, Practical [PSU]', 'Oxygen, SBE 43 [umol/kg]','O2[umol/kg], corrected', 'O2[umol/kg], checked', 'O2[umol/kg]', 'Date_Time']]
part.rename(columns={"O2[umol/kg], corrected":"Oxygen, Winkler [umol/kg]"}, inplace=True)   

# print(part[['Niskin_#', 'Depth [salt water, m]', 'Date_Time']].sort_values(by=['Niskin_#'], ascending=True))

# nn = str(part['Station'].unique()[0])

# folder='/Users/jung-ok/work1/ARA13B/processed/Winkler/'
folder='/Users/jung-ok/work1/'+cruise+'/processed/Winkler/LAB/'

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

file_name = '/Users/jung-ok/work1/'+cruise+'/plot/Winkler/LAB/depth_profile_winkler_ctd_'+cruise+st+'.png'

plt.suptitle(cruise+st)   
plt.savefig(file_name) 
plt.show()

print(i)
print('Done')


