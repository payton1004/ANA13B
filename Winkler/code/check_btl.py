import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress
import math

# *.btl 파일을 *.csv 파일로 저장한다.

# *.btl file,  
# Averaged and derived bottle data from .ros file, created by Bottle Summary

### cruise name ; change
# example: ANA13B
print("cruise: cruise name")
cruise = input("cruise = ")

# ANA13B 채수정점
# 총 7정점
# 1. 1
# 2. 41
# 3. 50 
# 4. 61
# 5. 80
# 6. 89 
# 7. 103

### before_ctd_btl.py 실행을 통해 header, _id를 확인한다.
# header : 컬럼명
# _id : 짝수행에서 NaN이 시작되기 직전 마지막 열의 인덱스

### change
header = ['Bottle', 'Month', 'Day', 'Year', 
'Salinity, Practical [PSU]', 'Salinity, Practical, 2 [PSU]',   
'Scan', 'Time, Elapsed [seconds]', 'Depth [salt water, m]',
'Temperature [ITS-90, deg C]', 'Temperature, 2 [ITS-90, deg C]',   
'Potential Temperature [ITS-90, deg C]', 
'Pressure, Digiquartz [db]', 'Conductivity [mS/cm]', 'Conductivity, 2 [mS/cm]',
'Specific Conductance [uS/cm]',
'Oxygen, SBE 43 [mg/l]', 'Oxygen, SBE 43 [umol/kg]', 'Oxygen Saturation, Weiss [ml/l]', 
'Beam Attenuation, WET Labs C-Star [1/m]',  'Fluorescence, WET Labs ECO-AFL/FL [mg/m^3]', 
'Latitude [deg]', 'Longitude [deg]',  'Julian Days', 
'Time', 
'Scan, sde', 'Elapsed, sde', 'Depth, sde',
'Temperature, sde', 'Temperature, 2, sde', 
'Potental Temperature, sde',       
'Pressure, sde', 'Conductivity, sde', 'Conductivity, 2, sde',   
'Specific Conductance, sde',
'Oxygen [mg/l], sde', 'Oxygen [umol/kg], sde', 'Weiss [ml/l], sde', 
'Beam Attenuation, sde',  'Fluorescence, sde', 
'Latitude, sde', 'Longitude, sde',  'Julian Days, sde']


btl_files = sorted(glob('/Users/jung-ok/work1/'+cruise+'/raw_data/CTD/LAB/bottle_summary/*.btl'))

# '/Users/jung-ok/work1/ANA13B/raw_data/CTD/LAB/bottle_summary/ANA13B001CTD1.btl', 
# '/Users/jung-ok/work1/ANA13B/raw_data/CTD/LAB/bottle_summary/ANA13B041CTD1.btl', 
# '/Users/jung-ok/work1/ANA13B/raw_data/CTD/LAB/bottle_summary/ANA13B050CTD1.btl', 
# '/Users/jung-ok/work1/ANA13B/raw_data/CTD/LAB/bottle_summary/ANA13B061CTD1.btl', 
# '/Users/jung-ok/work1/ANA13B/raw_data/CTD/LAB/bottle_summary/ANA13B080CTD1.btl', 
# '/Users/jung-ok/work1/ANA13B/raw_data/CTD/LAB/bottle_summary/ANA13B089CTD1.btl', 
# '/Users/jung-ok/work1/ANA13B/raw_data/CTD/LAB/bottle_summary/ANA13B103CTD1.btl'

old_folder='/Users/jung-ok/work1/'+cruise+'/raw_data/CTD/LAB/bottle_summary/'
new_folder='/Users/jung-ok/work1/'+cruise+'/raw_data/CTD/LAB/bottle_summary/new/'


# for j in np.arange(len(btl_files)):
# j = 93  
# btl=btl_files[j]
# # fname= btl.split('/')[-1]
# fname= btl.split('/')[-1]

# index
# 0, 1, 2, 3, 4, 5, 6
# station
# 001, 041, 050, 061, 080, 089, 103
print("Station Number")
st = input("st = ")

# cast
# 1
print("Cast Number")
cast = input("cast = ")

fname = cruise+st+'CTD'+cast+'.btl'
print(fname)

if st=='001':
    sr=245
elif st=='041':
    sr=244
elif st=='050':
    sr=244  
elif st=='061':
    sr=245    
elif st=='080':
    sr=245  
elif st=='089':
    sr=245    
elif st=='103':
    sr=245    

df= pd.read_csv(old_folder+fname,skiprows=sr, index_col=None, header=None, delimiter=r"\s+")


# odd row
df1=df.iloc[::2,:].reset_index(drop=True)
# even row
df2=df.iloc[1::2,:].reset_index(drop=True)

### change
# merge 
# df1.iloc[:,0:-1], 마지막 열 (avg) 제외
# df2.iloc[:,0:_id] NaN인 열들은 제외
if cruise == 'ANA13B':
    _id=19 #  
# elif cruise == 'ARA13B':
#     _id=20 #   

result = pd.concat([df1.iloc[:,0:-1], df2.iloc[:,0:_id]], axis=1)

result.columns = header
result['Date_Time']=result['Month']+'-'+result['Day'].astype(int).astype(str)+'-'+result['Year'].astype(int).astype(str)+' '+result['Time']
result[['Date_Time']+header].to_csv(new_folder+fname.split('.')[0]+'.csv', index=False, na_rep=np.nan, float_format='%g')

print('Done')

# ### 변환된 csv 파일을 불러와 확인한다.
# csv_files = sorted(glob(new_folder+'*.csv'))
# print("j: index of file list")
# k = int(input("k = "))
# df= pd.read_csv(csv_files[k], index_col=None, parse_dates=[0])
# print(df[['Date-Time', 'Bottle', 'Depth [salt water, m]', 'Oxygen, SBE 43 [umol/kg]']].head())
# print(df[['Date-Time', 'Latitude [deg]', 'Longitude [deg]']].head())