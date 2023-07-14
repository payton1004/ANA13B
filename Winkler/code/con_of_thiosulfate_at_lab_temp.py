import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress

### 파일 

# sampling stations
# ANA11A21, ANA11A36, ANA11A51, ANA11A72, ANA11A82, ANA11B56, ANA11B78
# i = [0, 1, 2, 3, 4, 5, 6]

# i = 0 (ANA11A21)
# bottle No.67 sample 버튼이 아닌 blank 버튼 누름 
# 18 (python은 0부터 시작, *.txt 파일상에서는 19행에 해당)

# i = 2 (ANA11A51)
# bottle No.33, 39 채수한 닛스킨번호 확실치 않음; 
# 15번 닛스킨 채수하려 했으나 윗뚜껑이 열리지 않았음
# 채수한 닛스킨 번호가 14번인지 16번인지 데이터 비교를 통해 확인해야 함

# i = 3 (ANA11A72)
# bottle No.52, 병번호를 51로 잘못 입력함

# i = 4 (ANA11A82)
# 17행(16)
# bottle No.65, n>30

# i = 5 (ANA11B56)
# 닛스킨 24개 중 9개만 터트림
# 닛스킨 번호 수정 
# (4,5,6)=>9,10,11 
# (7,8,9)=>17,18,19

# i = 6 (ANA11B78)
# 8-9행(7-8)
# bottle No.56, 57 뚜껑이 뒤바뀜



print("i: index of file list")
i = int(input("i = "))

# for i in range(7):
#     print(i)
#     ctd_files =sorted(glob('/Users/jung-ok/work1/ANA11/raw_data/ctd/bottle_summary/new/*.csv'))
#     winkler_files =sorted(glob('/Users/jung-ok/work1/ANA11/raw_data/winkler/new/*.csv'))
#     print(ctd_files[i].split('/')[-1], winkler_files[i].split('/')[-1])

### CTD sensor (항차명 + 정점번호)
# ANA11A21CTD1.csv	
# ANA11A36CTD1.csv 
# ANA11A51CTD1.csv 
# ANA11A72CTD1.csv	 
# ANA11A82CTD1.csv	
# ANA11B56CTD1.csv  
# ANA11B78CTD1.csv 

ctd_files =sorted(glob('/Users/jung-ok/work1/ANA11/raw_data/ctd/bottle_summary/new/*.csv'))
# print(ctd_files[i].split('/')[-1].split('.')[0][6:8])
cruise=ctd_files[i].split('/')[-1].split('.')[0][:6]
st_num=ctd_files[i].split('/')[-1].split('.')[0][6:8]

db = pd.read_csv(ctd_files[i], index_col=None,  parse_dates=[1])

# Rename column
db.rename(columns={"Bottle":"Niskin_#"}, inplace=True)  


### Winkler titrator (파일명: Run date + 채수장소 약어 + 정점번호)
# 0 20201210_TNB_st21.csv 
# 1 20201216_MPA_st36.csv
# 2 20201216_MPA_st51.csv
# 3 20201221_LAB_st72.csv
# 4 20201223_TNB_st82.csv
# 5 20210123_Sejong_st28.csv 
# 6 20210130_Sejong_st02.csv

winkler_files =sorted(glob('/Users/jung-ok/work1/ANA11/raw_data/winkler/new/*.csv'))
dw= pd.read_csv(winkler_files[i], index_col=None)
# Rename column
dw.rename(columns={"Depth":"Depth [salt water, m]"}, inplace=True)   



# for b in dw['Niskin'].unique():
#     print(b)
#     dw['Depth [salt water, m]'][dw[u'Niskin_#']==b]=db[u'Depth [salt water, m]'][db[u'Niskin_#']==b].to_list()

### 변경전
# print(dw[['Niskin_#', 'O2[umol/kg]']])
# print(db[['Niskin_#', 'Depth [salt water, m]']])


### Replace few values in a dataframe column with another value

if i==2 : 
    # 19-20행 (18-19)
    # 채수한 닛스킨 번호가 15번
    # Niskin_# 변경  15=>14 또는 15=>16 변경한 후 비교
    # dw['Niskin_#']=dw['Niskin_#'].replace([15], 16)
    # 결측값으로 간주, np.nan으로 변경
     dw['O2[uM]'][18]=np.nan ; dw['O2[umol/kg]'][18]=np.nan ; dw['End_Point'][18]=np.nan
     dw['O2[uM]'][19]=np.nan ; dw['O2[umol/kg]'][19]=np.nan ; dw['End_Point'][19]=np.nan
elif i==3 : 
    # 5행 (4)
    # 닛스킨 번호 11번을 7번으로 잘못 입력함
    # 병 번호 52번을 51번으로 잘못 입력함
     dw['Niskin_#'][4]=11
     dw['Bottle_#'][4]=52
     dw['O2[uM]'][4]=np.nan ; dw['O2[umol/kg]'][4]=np.nan 
     # 1행 (0) 
     # 결측값으로 간주, np.nan으로 변경
     dw['O2[uM]'][0]=np.nan ; dw['O2[umol/kg]'][0]=np.nan ; dw['End_Point'][0]=np.nan
elif i==4 : 
    # 17행 (16)
    # n>30
    # End point값을 직접 찾아야 함
    # 결측값으로 간주, np.nan으로 변경
     dw['O2[uM]'][16]=np.nan ; dw['O2[umol/kg]'][16]=np.nan ; dw['End_Point'][16]=np.nan 
elif i==5 : 
    # CTD bottle summary 닛스킨 번호 수정
     db['Niskin_#'][3]=9
     db['Niskin_#'][4]=10 
     db['Niskin_#'][5]=11
     db['Niskin_#'][6]=17 
     db['Niskin_#'][7]=18
     db['Niskin_#'][8]=19  
elif i==6 : 
    # 8-9행 (7-8)
    # 뚜껑과 몸체 번호가 다름
    # 결측값으로 간주, np.nan으로 변경
     dw['O2[uM]'][7]=np.nan ; dw['O2[umol/kg]'][7]=np.nan ; dw['End_Point'][7]=np.nan 
     dw['O2[uM]'][8]=np.nan ; dw['O2[umol/kg]'][8]=np.nan ; dw['End_Point'][8]=np.nan        
              
      

### 변경후 
# print(dw[['Niskin_#', 'O2[umol/kg]']])
# print(db[['Niskin_#', 'Depth [salt water, m]']])


### Temperature
# (winkler)
# 'Thio_Temp(degC)' Laboratory Temperature, Preparation Temperature
# 'Draw_Temp(degC)' Sampling Temperature
# (ctd)
# 'Temperature [ITS-90, deg C]' Sampling Temperature


### merge (Winkler titrator, CTD sensor, flask volumes)
winkler=dw[['Station','Niskin_#', 'Bottle_#', 'Std_Tit', 'Blk_Tit','End_Point', \
'Thio_Temp(degC)', 'Thio_Density', 'M(Thio tL)', 'M(Thio 20C)', 'Draw_Temp(degC)', 'Salinity', 'SW_density', 'O2[uM]',  'O2[umol/kg]']]

# ANA11
ctd=db[['Date_Time','Latitude [deg]', 'Longitude [deg]', 'Niskin_#', 'Depth [salt water, m]', 'Oxygen, SBE 43 [umol/kg]', \
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


# Volume for Standard titrating
# Volume for Blank titrating

do_table['M(Thio tL), corrected'] = 6000 * do_table['V(KIO3 tL)'] * do_table['M(KIO3 tp)'] / (do_table['Std_Tit'] - do_table['Blk_Tit'])

print(do_table[['M(Thio tL), corrected','M(Thio tL)']])



# ### calculte 'O2[uM]' from 'End_Point'
# do_table['O2[mol]']=(do_table['End_Point'] - do_table['Blk_Tit'])*do_table['M(Thio tL)']*1E-6*0.25

# do_table['O2[uM], checked']=((do_table['O2[mol]']-7.6*1E-8)/((do_table[u'Vol @20C']*(1+9.75*1E-6*(do_table[u'Draw_Temp(degC)']-20))-2)*1E-3))*1E6
# do_table['O2[uM], corrected']=((do_table['O2[mol]']-7.6*1E-8)/((do_table[u'Vol @20C']*(1+9.75*1E-6*(do_table[u'Temperature [ITS-90, deg C]']-20))-2)*1E-3))*1E6

# ##### O2[uM]
# # do_table[['O2[uM]','O2[uM], checked', 'O2[uM], corrected']]


# do_table['SMOW, checked'] =  999.842594 + 6.793952 * 1E-2 * do_table[u'Draw_Temp(degC)'] - 9.095290 * 1E-3 * do_table[u'Draw_Temp(degC)']**2 + 1.001685 * 1E-4 * do_table[u'Draw_Temp(degC)']**3 \
#  - 1.120083 * 1E-6 * do_table[u'Draw_Temp(degC)']**4 + 6.536332 * 1E-9 * do_table[u'Draw_Temp(degC)']**5

# do_table['A, checked'] =  8.24493 * 1E-1 - 4.0899 * 1E-3 * do_table[u'Draw_Temp(degC)'] + 7.6438 * 1E-5 * do_table[u'Draw_Temp(degC)']**2 - 8.2467 * 1E-7 * do_table[u'Draw_Temp(degC)']**3+ 5.3875 * 1E-9 * do_table[u'Draw_Temp(degC)']**4 

# do_table['B, checked'] = -5.72466 * 1E-3 + 1.0227 * 1E-4 * do_table[u'Draw_Temp(degC)']- 1.6546 * 1E-6 * do_table[u'Draw_Temp(degC)']**2  

# do_table['C, checked'] = 4.8314 * 1E-4

# do_table['SW_density, checked'] = (do_table['SMOW, checked'] + do_table['A, checked']*do_table['Salinity'] + do_table['B, checked']*do_table['Salinity']**1.5 + do_table['C, checked'] * do_table['Salinity']**2)*1E-3


# do_table['SMOW, corrected'] = 999.842594 + 6.793952 * 1E-2 * do_table[u'Temperature [ITS-90, deg C]'] - 9.095290 * 1E-3 * do_table[u'Temperature [ITS-90, deg C]']**2 + 1.001685 * 1E-4 * do_table[u'Temperature [ITS-90, deg C]']**3  \
#  - 1.120083 * 1E-6 * do_table[u'Temperature [ITS-90, deg C]']**4 + 6.536332 * 1E-9 * do_table[u'Temperature [ITS-90, deg C]']**5

# do_table['A, corrected'] = 8.24493 * 1E-1 - 4.0899 * 1E-3 * do_table[u'Temperature [ITS-90, deg C]']+ 7.6438 * 1E-5 * do_table[u'Temperature [ITS-90, deg C]']**2 - 8.2467 * 1E-7 * do_table[u'Temperature [ITS-90, deg C]']**3+ 5.3875 * 1E-9 * do_table[u'Temperature [ITS-90, deg C]']**4 

# do_table['B, corrected'] = -5.72466 * 1E-3 + 1.0227 * 1E-4 * do_table[u'Temperature [ITS-90, deg C]']- 1.6546 * 1E-6 * do_table[u'Temperature [ITS-90, deg C]']**2  

# do_table['C, corrected'] = 4.8314 * 1E-4

# do_table['SW_density, corrected'] = (do_table['SMOW, corrected'] + do_table['A, corrected'] * do_table['Salinity, Practical [PSU]'] + do_table['B, corrected'] * do_table['Salinity, Practical [PSU]']**1.5 + do_table['C, corrected'] * do_table['Salinity, Practical [PSU]']**2)*1E-3

# ##### SW_density
# # do_table[['SW_density','SW_density, checked', 'SW_density, corrected']]
# ##### 

# ##### 
# do_table['O2[umol/kg], checked']=do_table['O2[uM]']/do_table[u'SW_density']
# do_table['O2[umol/kg], corrected']=do_table['O2[uM], corrected']/do_table[u'SW_density, corrected']

# ##### O2[umol/kg] , Oxygen, SBE 43 [umol/kg]
# # do_table[['Depth [salt water, m]','O2[umol/kg]','O2[umol/kg], checked', 'O2[umol/kg], corrected', u'Oxygen, SBE 43 [umol/kg]']]

# # co=do_table[['Depth [salt water, m]', 'O2[umol/kg], corrected', u'Oxygen, SBE 43 [umol/kg]']]
# # co.columns=['Depth [salt water, m] [m]', 'O2 [umol/kg], Winkler', u'Oxygen, SBE 43 [umol/kg]']
# part=do_table[['Station', 'Latitude [deg]', 'Longitude [deg]','Niskin_#', 'Depth [salt water, m]', 'Bottle_#', \
#  'Temperature [ITS-90, deg C]', 'Salinity, Practical [PSU]', 'Oxygen, SBE 43 [umol/kg]','O2[umol/kg], corrected', 'O2[umol/kg]','Date_Time']]
# part.rename(columns={"O2[umol/kg], corrected":"Oxygen, Winkler [umol/kg]"}, inplace=True)   

# # print(part[['Niskin_#', 'Depth [salt water, m]', 'Date_Time']].sort_values(by=['Niskin_#'], ascending=True))

# # nn = str(part['Station'].unique()[0])

# folder='/Users/jung-ok/work1/ANA11/processed/winkler/'

# # print(i)

# # if i==0:
# #    file_name = 'dissolved_oxygen_Winkler_CTD_st'+'0'+nn+'.csv'
# # else:
# #    file_name = 'dissolved_oxygen_Winkler_CTD_st'+nn+'.csv'

# file_name = 'dissolved_oxygen_Winkler_CTD_'+cruise+st_num+'.csv'

# # print(folder+file_name)

# # part.sort_values(by=['Niskin_#'], ascending=True).to_csv(folder+file_name, index=False, na_rep=np.nan, float_format='%5.3f')

# # 1: winkler titrator, 2: winkler 자료를 (온도, 염분)값에 의한 보정,  3: CTD SBE sensor 
# # (1-2), (1-3), (2-3)
# # 최종적으로 winkler 보정값과 CTD sensor 값을 비교
# do_table['winkler-corrected'] = do_table['O2[umol/kg]']-do_table['O2[umol/kg], corrected']
# do_table['winkler-SBE'] = do_table['O2[umol/kg]']-do_table['Oxygen, SBE 43 [umol/kg]']        
# do_table['corrected-SBE'] = do_table['O2[umol/kg], corrected'] - do_table[u'Oxygen, SBE 43 [umol/kg]']
    
# print(do_table[['Depth [salt water, m]','winkler-corrected','winkler-SBE','corrected-SBE']])





