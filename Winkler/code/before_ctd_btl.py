import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import datetime
import string
from scipy.stats import linregress
import math

### header, _id를 결정한다.
# header : 컬럼명
# _id : 짝수행에서 NaN이 시작되기 직전 마지막 열의 인덱스

# *.btl 파일, 항목 선택에 따라 컬럼의 갯수와 순서가 다르다.
# 연이은 (홀수행과 짝수행)이 하나의 행으로 변환해야 함.
# 홀수행에서 마지막 열 (avg)을,
# 짝수행에서 NaN인 열들을 제외한다.


### cruise name 
# example: ANA13B
print("cruise: cruise name")
cruise = input("cruise = ")

# 코드 변경
if cruise == 'ANA13B':
    btl_files = sorted(glob('/Users/jung-ok/work1/'+cruise+'/raw_data/CTD/LAB/bottle_summary/*.btl'))
# elif cruise == 'ARA13B':
    # btl_files = sorted(glob('/Users/jung-ok/work1/'+cruise+'/raw_data/CTD/bottle_summary/*.btl'))

for i, fname in enumerate(btl_files):
    print(i, fname)

# ANA13B
# sampling stations:  
# 1, 41, 50, 61, 80, 89, 103
# index
# 0, 1, 2, 3, 4, 5, 6 

if cruise == 'ANA13B':
    old_folder='/Users/jung-ok/work1/'+cruise+'/raw_data/CTD/LAB/bottle_summary/'
    new_folder='/Users/jung-ok/work1/'+cruise+'/raw_data/CTD/LAB/bottle_summary/new/'
# elif cruise == 'ARA13B':
#     old_folder='/Users/jung-ok/work1/'+cruise+'/raw_data/CTD/bottle_summary/'
#     new_folder='/Users/jung-ok/work1/'+cruise+'/raw_data/CTD/bottle_summary/new/'

# 불러올 파일을 선택한다.
print("j: index of file list")
j = int(input("j = "))

# j = 0
# ANA13B001CTD1.btl

#
btl=btl_files[j]
fname= btl.split('/')[-1] 
print(fname)

# *.btl 파일을 열어 몇 행부터 읽을지를 선택한다. 
if j==0:
    sr=245
elif j==1:
    sr=244
elif j==2:
    sr=244  
elif j==3:
    sr=245    
elif j==4:
    sr=245  
elif j==5:
    sr=245    
elif j==6:
    sr=245            

df= pd.read_csv(old_folder+fname, skiprows=sr, index_col=None, header=None, delimiter=r"\s+")    

# odd row
df1=df.iloc[::2,:].reset_index(drop=True)
# even row
df2=df.iloc[1::2,:].reset_index(drop=True)

# merge 
# df1.iloc[:,0:-1], 마지막 열 (avg) 제외
# df2.iloc[:,0:_id] NaN인 열들은 제외
if cruise == 'ANA13B':
    _id=19 #  
# elif cruise == 'ARA13B':
#     _id=20 #     

result = pd.concat([df1.iloc[:,0:-1], df2.iloc[:,0:_id]], axis=1) # 왼쪽(홀수행)+오른쪽(짝수행) dataframe 합치기 

### 수정해야 함
if cruise == 'ANA13B':
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
# elif cruise == 'ARA13B':
#  header = ['Bottle', 'Month', 'Day', 'Year', 
# 'Scan', 'Time, Elapsed [seconds]', 'Depth [salt water, m]',
# 'Temperature [ITS-90, deg C]', 'Temperature, 2 [ITS-90, deg C]',      
# 'Pressure, Digiquartz [db]', 'Conductivity [mS/cm]', 'Conductivity, 2 [mS/cm]',
# 'Salinity, Practical [PSU]', 'Salinity, Practical, 2 [PSU]',  'Specific Conductance [uS/cm]',
# 'Oxygen, SBE 43 [mg/l]', 'Oxygen, SBE 43 [umol/kg]', 'Oxygen Saturation, Weiss [ml/l]', 
# 'Beam Attenuation, WET Labs C-Star [1/m]',  'Fluorescence, WET Labs ECO-AFL/FL [mg/m^3]', 
# 'Latitude [deg]', 'Longitude [deg]',  'Julian Days', 
# 'Time', 'Scan, sde', 'Elapsed, sde', 'Depth, sde',
# 'Temperature, sde', 'Temperature, 2, sde',      
# 'Pressure, sde', 'Conductivity, sde', 'Conductivity, 2, sde', 
# 'Salinity, sde', 'Salinity, 2, sde', 
# 'Specific Conductance, sde',
# 'Oxygen [mg/l], sde', 'Oxygen [umol/kg], sde', 'Weiss [ml/l], sde', 
# 'Beam Attenuation, sde',  'Fluorescence, sde', 
# 'Latitude, sde', 'Longitude, sde',  'Julian Days, sde']

result.columns = header

# 새로운 컬럼 'Date-Time' 생성
result['Date_Time']=result['Month']+'-'+result['Day'].astype(int).astype(str)+'-'+result['Year'].astype(int).astype(str)+' '+result['Time']

# 출력결과를 보고 header, _id가 적절했는지 알 수 있다. 
print(result[['Date_Time', 'Bottle', 'Depth [salt water, m]', 'Oxygen, SBE 43 [umol/kg]']].head())

# 깊이별 해수용존산소농도 그래프를 그린다.
fig, ax= plt.subplots(1, 1, figsize=(5, 8) ,sharex=True)
result.plot(y='Depth [salt water, m]', x='Oxygen, SBE 43 [umol/kg]', sharex=True, ax=ax, label='bottle summary' , linestyle=' ', marker='o', alpha=0.25, ms=5, clip_on=False, zorder=100)
ax.set_ylim(result['Depth [salt water, m]'].max(), 0)
plt.show()